# Custom Cart Generator

Shopify application for creating and sharing custom carts.

## Download

Clone the repository by running one of the following commands.  
`git clone git@github.com:SoftDevInc/UserManagementSystem.git`  
or  
`git clone https://github.com/SoftDevInc/UserManagementSystem.git`

## Installation

Install the Python dependencies by running `pip install -r requirements.txt`.  
Install the NPM dependencies by running `npm install`.  

## Usage
### Frontend

This app is built using the Svelte framework. To run and test locally run `npm run dev`. This
will start a local development server that will watch the local file system and update
with any changes you make within the `src` folder.

### Backend

The backend can be run locally by running `npm run offline`. This runs `serverless offline start`
under the hood.

### Deployment

Deploy both the frontend and backend by running `npm run deploy`. It will run `serverless deploy` under the hood
to deploy out all the AWS resources. Then it will create a production build of the Svelte frontend and 
then copy it out to the S3 bucket defined within the `serverless-resources.yml` file. All the resources created by the
deployment process will save their variables (names, arns, etc.) to `stack.yml`.
