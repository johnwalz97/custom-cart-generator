
/**
 * @roxi/routify 2.15.1
 * File generated Tue Apr 20 2021 00:00:16 GMT-0400 (Eastern Daylight Time)
 */

export const __version = "2.15.1"
export const __timestamp = "2021-04-20T04:00:16.384Z"

//buildRoutes
import { buildClientTree } from "@roxi/routify/runtime/buildRoutes"

//imports


//options
export const options = {}

//tree
export const _tree = {
  "name": "_layout",
  "filepath": "/_layout.svelte",
  "root": true,
  "ownMeta": {},
  "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/_layout.svelte",
  "children": [
    {
      "isFile": true,
      "isDir": false,
      "file": "_fallback.svelte",
      "filepath": "/_fallback.svelte",
      "name": "_fallback",
      "ext": "svelte",
      "badExt": false,
      "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/_fallback.svelte",
      "importPath": "../src/pages/_fallback.svelte",
      "isLayout": false,
      "isReset": false,
      "isIndex": false,
      "isFallback": true,
      "isPage": false,
      "ownMeta": {},
      "meta": {
        "recursive": true,
        "preload": false,
        "prerender": true
      },
      "path": "/_fallback",
      "id": "__fallback",
      "component": () => import('../src/pages/_fallback.svelte').then(m => m.default)
    },
    {
      "isFile": true,
      "isDir": false,
      "file": "index.svelte",
      "filepath": "/index.svelte",
      "name": "index",
      "ext": "svelte",
      "badExt": false,
      "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/index.svelte",
      "importPath": "../src/pages/index.svelte",
      "isLayout": false,
      "isReset": false,
      "isIndex": true,
      "isFallback": false,
      "isPage": true,
      "ownMeta": {},
      "meta": {
        "recursive": true,
        "preload": false,
        "prerender": true
      },
      "path": "/index",
      "id": "_index",
      "component": () => import('../src/pages/index.svelte').then(m => m.default)
    },
    {
      "isFile": true,
      "isDir": true,
      "file": "_reset.svelte",
      "filepath": "/oauth/_reset.svelte",
      "name": "_reset",
      "ext": "svelte",
      "badExt": false,
      "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/oauth/_reset.svelte",
      "children": [
        {
          "isFile": true,
          "isDir": false,
          "file": "index.svelte",
          "filepath": "/oauth/index.svelte",
          "name": "index",
          "ext": "svelte",
          "badExt": false,
          "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/oauth/index.svelte",
          "importPath": "../src/pages/oauth/index.svelte",
          "isLayout": false,
          "isReset": false,
          "isIndex": true,
          "isFallback": false,
          "isPage": true,
          "ownMeta": {},
          "meta": {
            "recursive": true,
            "preload": false,
            "prerender": true
          },
          "path": "/oauth/index",
          "id": "_oauth_index",
          "component": () => import('../src/pages/oauth/index.svelte').then(m => m.default)
        },
        {
          "isFile": true,
          "isDir": false,
          "file": "redirect.svelte",
          "filepath": "/oauth/redirect.svelte",
          "name": "redirect",
          "ext": "svelte",
          "badExt": false,
          "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/oauth/redirect.svelte",
          "importPath": "../src/pages/oauth/redirect.svelte",
          "isLayout": false,
          "isReset": false,
          "isIndex": false,
          "isFallback": false,
          "isPage": true,
          "ownMeta": {},
          "meta": {
            "recursive": true,
            "preload": false,
            "prerender": true
          },
          "path": "/oauth/redirect",
          "id": "_oauth_redirect",
          "component": () => import('../src/pages/oauth/redirect.svelte').then(m => m.default)
        }
      ],
      "isLayout": true,
      "isReset": true,
      "isIndex": false,
      "isFallback": false,
      "isPage": false,
      "importPath": "../src/pages/oauth/_reset.svelte",
      "ownMeta": {},
      "meta": {
        "recursive": true,
        "preload": false,
        "prerender": true
      },
      "path": "/oauth",
      "id": "_oauth__reset",
      "component": () => import('../src/pages/oauth/_reset.svelte').then(m => m.default)
    },
    {
      "isFile": false,
      "isDir": true,
      "file": "templates",
      "filepath": "/templates",
      "name": "templates",
      "ext": "",
      "badExt": false,
      "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/templates",
      "children": [
        {
          "isFile": true,
          "isDir": false,
          "file": "[template_id].svelte",
          "filepath": "/templates/[template_id].svelte",
          "name": "[template_id]",
          "ext": "svelte",
          "badExt": false,
          "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/templates/[template_id].svelte",
          "importPath": "../src/pages/templates/[template_id].svelte",
          "isLayout": false,
          "isReset": false,
          "isIndex": false,
          "isFallback": false,
          "isPage": true,
          "ownMeta": {},
          "meta": {
            "recursive": true,
            "preload": false,
            "prerender": true
          },
          "path": "/templates/:template_id",
          "id": "_templates__template_id",
          "component": () => import('../src/pages/templates/[template_id].svelte').then(m => m.default)
        },
        {
          "isFile": true,
          "isDir": false,
          "file": "choose_discount.svelte",
          "filepath": "/templates/choose_discount.svelte",
          "name": "choose_discount",
          "ext": "svelte",
          "badExt": false,
          "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/templates/choose_discount.svelte",
          "importPath": "../src/pages/templates/choose_discount.svelte",
          "isLayout": false,
          "isReset": false,
          "isIndex": false,
          "isFallback": false,
          "isPage": true,
          "ownMeta": {},
          "meta": {
            "recursive": true,
            "preload": false,
            "prerender": true
          },
          "path": "/templates/choose_discount",
          "id": "_templates_choose_discount",
          "component": () => import('../src/pages/templates/choose_discount.svelte').then(m => m.default)
        },
        {
          "isFile": true,
          "isDir": false,
          "file": "choose_products.svelte",
          "filepath": "/templates/choose_products.svelte",
          "name": "choose_products",
          "ext": "svelte",
          "badExt": false,
          "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/templates/choose_products.svelte",
          "importPath": "../src/pages/templates/choose_products.svelte",
          "isLayout": false,
          "isReset": false,
          "isIndex": false,
          "isFallback": false,
          "isPage": true,
          "ownMeta": {},
          "meta": {
            "recursive": true,
            "preload": false,
            "prerender": true
          },
          "path": "/templates/choose_products",
          "id": "_templates_choose_products",
          "component": () => import('../src/pages/templates/choose_products.svelte').then(m => m.default)
        },
        {
          "isFile": true,
          "isDir": false,
          "file": "index.svelte",
          "filepath": "/templates/index.svelte",
          "name": "index",
          "ext": "svelte",
          "badExt": false,
          "absolutePath": "/home/jwalz/Code/Personal/custom-cart-generator/src/pages/templates/index.svelte",
          "importPath": "../src/pages/templates/index.svelte",
          "isLayout": false,
          "isReset": false,
          "isIndex": true,
          "isFallback": false,
          "isPage": true,
          "ownMeta": {},
          "meta": {
            "recursive": true,
            "preload": false,
            "prerender": true
          },
          "path": "/templates/index",
          "id": "_templates_index",
          "component": () => import('../src/pages/templates/index.svelte').then(m => m.default)
        }
      ],
      "isLayout": false,
      "isReset": false,
      "isIndex": false,
      "isFallback": false,
      "isPage": false,
      "ownMeta": {},
      "meta": {
        "recursive": true,
        "preload": false,
        "prerender": true
      },
      "path": "/templates"
    }
  ],
  "isLayout": true,
  "isReset": false,
  "isIndex": false,
  "isFallback": false,
  "isPage": false,
  "isFile": true,
  "file": "_layout.svelte",
  "ext": "svelte",
  "badExt": false,
  "importPath": "../src/pages/_layout.svelte",
  "meta": {
    "recursive": true,
    "preload": false,
    "prerender": true
  },
  "path": "/",
  "id": "__layout",
  "component": () => import('../src/pages/_layout.svelte').then(m => m.default)
}


export const {tree, routes} = buildClientTree(_tree)

