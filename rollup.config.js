import dotenv from 'dotenv';
import svelte from 'rollup-plugin-svelte-hot';
import Hmr from 'rollup-plugin-hot';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import { terser } from 'rollup-plugin-terser';
import { copySync, removeSync } from 'fs-extra';
import getConfig from '@roxi/routify/lib/utils/config';
import autoPreprocess from 'svelte-preprocess';
import postcssImport from 'postcss-import';

dotenv.config();

const { distDir } = getConfig();
const assetsDir = 'assets';
const buildDir = `${distDir}/build`;
const isNollup = !!process.env.NOLLUP;
const production = !process.env.ROLLUP_WATCH;

removeSync(distDir);
removeSync(buildDir);

const copyToDist = () => ({
  writeBundle() {
    copySync(assetsDir, distDir);
  },
});

export default {
  preserveEntrySignatures: false,
  input: [`src/main.js`],
  output: {
    sourcemap: true,
    format: 'esm',
    dir: buildDir,
    chunkFileNames: `[name]${production && '-[hash]' || ''}.js`,
  },
  plugins: [
    svelte({
      dev: !production,
      css: css => css.write(`bundle.css`),
      hot: isNollup,
      preprocess: [
        autoPreprocess({
          postcss: { plugins: [postcssImport()] },
          defaults: { style: 'postcss' },
          scss: {
            includePaths: ['src/theme'],
          }
        }),
      ],
    }),
    resolve({
      browser: true,
      preferBuiltins: false,
      dedupe: importee => !!importee.match(/svelte(\/|$)/),
    }),
    commonjs(),
    !production && isNollup && Hmr({ inMemory: true, public: assetsDir }),
    {
      transform: code => {
        code = code.replace(/process.env.NODE_ENV/g, `"${process.env.NODE_ENV || 'dev'}"`);
        code = code.replace(/process.env.SHOPIFY_API_KEY/g, `"${process.env.SHOPIFY_API_KEY}"`);
        code = code.replace(/process.env.SHOPIFY_API_SECRET/g, `"${process.env.SHOPIFY_API_SECRET}"`);

        return {
          code: code,
          map: { mappings: '' },
        }
      },
    },
    production && terser(),
    production && copyToDist(),
  ],
  watch: {
    clearScreen: false,
    buildDelay: 100,
  },
};
