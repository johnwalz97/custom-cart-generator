#!/bin/bash

deploy() {
  local env=${1:-"dev"}

  echo "~~~ Starting deployment of $env environment"
  echo ""

  # deploy AWS Lambda backend
  echo "~~~ Deploying AWS Lambda backend"
  ./node_modules/.bin/serverless deploy --stage "$env"
  echo ""

  # deploy Svelte frontend to S3
  echo "~~~ Deploying Svelte frontend to AWS S3"
  echo "~~~ Targeting public-read AWS S3 Bucket acl"
  rm -rf public/build
  npm run build
  aws s3 cp public s3://ccg-"$env"-frontend --recursive --cache-control max-age=0,no-cache,no-store,must-revalidate --acl public-read --profile personal
  echo ""

  echo "~~~ Deployment complete"
}

deploy "$@"
