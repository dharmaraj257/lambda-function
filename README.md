# Install Python Dependency and Libraries on AWS Lambda

### Step 1: Create a lambda function file.
1. Create a folder and open it with IDE.
2. Write a lambda function file.

### Step 2: Create an AWS Deployment Package.
1. Install Pandas
```
pip install --platform manylinux2014_x86_64 --target=package --implementation cp --python-version 3.10 --only-binary=:all: --upgrade pandas
```
3. Install Numpy
```
pip install --platform manylinux2014_x86_64 --target=package --implementation cp --python-version 3.10 --only-binary=:all: --upgrade numpy
```
4. Install Request
```
pip install --platform manylinux2014_x86_64 --target=package --implementation cp --python-version 3.10 --only-binary=:all: --upgrade requests
```
### Step 3: Create a zip folder with libraries.
1. Copy all libraries into the main folder (lambda-function)and delete the empty package.
2. Create and compress all content into a zip folder

### Step 4: Create a Lambda Function using AWS Management Console.
1. Go to the AWS account select lambda and open Create a lambda function.
2. Select Author from scratch and give the function name 
3. Select runtime as per your Python local version python 3.10
4. Other settings are the same as default and Click the create function.

### Step 5: Upload zip folder to lambda function
1. Click Upload from and select the zip folder 
2. Click upload select zip file and save.

### Step 6: Create a test event and test the lambda function.
1. Go to test and select test new event.
2. Leave default everything and save

## Output:
&nbsp;
![Lambda function](https://github.com/dharmaraj257/lambda-function/assets/100831265/b4c1d6e2-8f55-46cd-8dbc-138a63e12e55)
