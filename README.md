<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/asheshd/pset2_cc">
    <img src="https://user-images.githubusercontent.com/42042450/177474268-1d6921e1-7af0-4d32-9eed-22f64e37f6d7.png" alt="Logo" width="80" height="80">
  </a>

<h2 align="center"> PSet 2 MLOps project with data science Cookie-Cutter, DVC, CML, AWS S3 and Github actions for IISc</h2>

  <p align="center">
  This project caters to complete MLOps cycle of model training, deployment and serving with the help of full MLOps stacks using technologies like: DVC, CML, AWS S3 storage and Github-Actions. The project structure is created with datascience cookie-cutter starter project. It uses simple sklearn based neural network library and performs Multi Layer Perceptron Classifier based model training. The model is deployed to AWS S3 storage with test and production environment. Subsequently, this mode is retrieved from AWS S3 bucket and consumed to make prediction on feature dataset. The entire MLOps cycle is automated. 
    <br />
    <a href="https://github.com/asheshd/pset2_cc"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/asheshd/pset2_cc/pull/7#commitcomment-77390882">View Demo</a>
    ·
    <a href="https://github.com/asheshd/pset2_cc">Report Bug</a>
    ·
    <a href="https://github.com/asheshd/pset2_cc">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#results">Results</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
  The goal of this project to use full MLOps stack and create a complete forward and backward cycle.
  
This project caters to complete MLOps cycle of model training, deployment and serving with the help of full MLOps stacks using technologies like: DVC, CML, AWS S3 storage and Github-Actions. The project structure is created with datascience cookie-cutter starter project. It uses simple sklearn based neural network library and performs Multi Layer Perceptron Classifier based model training. The model is deployed to AWS S3 storage with test and production environment. Subsequently, this mode is retrieved from AWS S3 bucket and consumed to make prediction on feature dataset. The entire MLOps cycle is automated.
  
The tools used in achieving this goal are presented in the figure below, along with the flow of control/data.


![IISc MLOps Project](https://user-images.githubusercontent.com/42042450/177289974-1e8c5308-74ca-432e-985d-670a19d0dd31.png)

<p align="right">(<a href="#top">back to top</a>)</p>

### The chain and the tools are as follow:
#### Dataset Access

The datset is created with sklearn random make_classisfication with 100000 sets.
    
#### Integration using GitHub, DVC, CML and GitHub Actions and Training

GitHub is used for version control of the project's core ML training and model generation codes. Additionally, it is also maintaining the code to serve the updated model to the web application.

CML and DVC.
    
GitHub Actions is the main orchestrator in the flow. Whenever the repositories are updated, it runs the corresponding action scripts (.yaml). Whenever the main project is updated, the GitHub Actions workflow establishes an environment with python3 and installs all the requirements from the requirements.txt file. The requirements include libraries like tensorflow, keras, modelstore, boto3, and other common libraries. Tensorflow and keras are needed to execute the script for training the model from scratch on cloud. Boto3 and modelstore are required to generate the model in a format that AWS S3 supports for model hosting. Additionally, the keys required to make seamless access to AWS are defined in the yaml file while they are stored as secrets.
    
GitHub Actions also triggers the back-end project for the web application on every update. In order to setup the environment for calling the model from web application another set of requirements are installed which are same as the previous set of requirements. GitHub actions runs the script to call streamlit web application.
    
#### Model Deployment to AWS S3 bucket
The model is deployed to the Amazon AWS s3 bucket where it is launched to be consumed in any service. The modelstore library provides simple APIs to save and load the ML model from any authorised tool.
    
#### Model querying and serving on web
The web hosting application resides is called from GitHub Actions. The underlying script also loads the S3 model from AWS. Streamlit tool provides a fast and easy framework with many easy-to-use APIs that can be called from a python script. In this project, it is called from the GitHub project. It provides a simple and fast UI to query the underlying model and see the results immediately on the page.

### Web App

https://github.com/asheshd/MLOps-IISc-Proj-UI - A web UI project to serve model for AWS and make prediction for the top N movies recommendation.


### Built With

* [Python3](https://www.python.org/downloads/)
* [CML](https://cml.dev/)
* [DVC](https://dvc.org/)
* [Amazon AWS](https://aws.amazon.com/)
* [Data Science Cookiecutter](https://drivendata.github.io/cookiecutter-data-science/)
* [Github Action](https://github.com/features/actions)
* [SKlearn](https://scikit-learn.org/stable/)
* [ModelStore](https://pypi.org/project/modelstore/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Follow the below steps to get started with the this Recommendation System MLOps project.

### Prerequisites

Here is a list of python packages required to run this project.
* python
  ```sh
  numpy
  pandas
  dvc
  boto3
  modelstore
  sklearn
  matplotlib
  click
  Sphinx
  coverage
  awscli
  flake8
  python-dotenv>=0.5.1
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/asheshd/pset2_cc.git
   ```
3. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
   
4. Run make dataset
   ```sh
   python src/data/make_dataset.py
   ```
4. Run model training
   ```sh
   python src/models/train_model.py
   ```
5. Run model prediction
   ```sh
   python src/models/predict_model.py
   ```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Results

The following screenshot shows the metric data from the model training and prediction. The improvement in accuracy, precision and recall can be clearly seen in the indicator.

![Metrics](https://user-images.githubusercontent.com/42042450/177474268-1d6921e1-7af0-4d32-9eed-22f64e37f6d7.png)


_For more details, please refer to the [Web App](https://asheshd-mlops-iisc-proj-ui-predict-movies-j2nd76.streamlitapp.com/)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- Project Structure -->
## Project Structure


The project structure of this MLOPs pset2_cc project is as follows: - 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data from sklearn make_classification
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features classification for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models with Multi layered Perceptron of sklearn Neural network and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

* Ashesh Deep - asheshdeep@iisc.ac.in

Project Link: [https://github.com/asheshd/pset2_cc](https://github.com/asheshd/pset2_cc)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Prof. Sashikumaar Ganeshan
* Thivin Anandh

<p align="right">(<a href="#top">back to top</a>)</p>
