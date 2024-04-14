## Azure ML

### Setup 
To practice azure ml and to be able to run the codes provided here, you will need to setup:

- Azure ML Workspace
- Storage Account
- Setup azure-ml cli
- Setting up azure-environment locally

You will have to create an azure account for that and you can expect cloud bill ranging from $25-75 (depending on how you use the resources).

#### Setting up Azure ML Workspace

Follow this [link](https://learn.microsoft.com/en-IN/azure/machine-learning/quickstart-create-resources?view=azureml-api-2) to setup an azure-ml workspace. Not at this stage you don't need to setup a **compute instance**

#### Setting up Storage Account

Follow this [link](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal) to create an azure storage account. Its advisable to create an azure datalake gen2 account.

#### Setting up azure-cli

Follow this [link](https://learn.microsoft.com/en-in/azure/machine-learning/how-to-configure-cli?view=azureml-api-2&tabs=public)


#### Setting up azure-environment locally
Use the [env.yaml](../../env.yaml) to setup a local environment. 

If you are using apple-silicon based computer you will need to remove `azureml-fsspec<=1.3.0` from the env file before setting up thee environment and you will not be able to run all the codes provided here on your local setup. You can setup a compute in the azure-ml workspace and create an environment there to run the codes provided here.

## Working with datasets in azure-ml

Before you can start building a model you need a way to manage and version control your data. Azure-ml provides an easy way to work with data.

Refer to [`datasets_azure_ml`](./datasets_azure_ml/) for the notebooks and further lecture notes.

## Creating compute environments in azure-ml

To train a model on either an azure-ml compute or compute cluster, one needs to define what ml libraries will be used. For reproducibility of runs, one needs to also specify the versions of these libraries. Azure-ml has `Environment` abstraction.

Refer to [`environments_azure_ml`](./environments_azure_ml/) for the notebooks and further lecture notes.

## Creating training pipeline components

The next important abstraction is the one in which we start creating model training components.

Refer to [`components_azure_ml`](./components_azure_ml/) for the notebooks and further lecture notes.

## Creating training pipeline

Once we know how to create components, lets look at how we can create a pipeline using the components.

Refer to [`pipelines_azure_ml`](./pipelines_azure_ml/) for the notebooks and further lecture notes.

## Deployment in azure ml

Once the model has been trained, we will need to deploy the model. Azure ml provides following options for model deployment:

1. Online deployments: This creates an api service to consume the model created.

2. Batch deployments: This creates a service that can do bulk predictions.

Refer to [`deployment_azure_ml`](./deployment_azure_ml/) for the notebooks and further lecture notes.