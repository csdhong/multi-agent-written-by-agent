from projen.awscdk import AwsCdkPythonApp

project = AwsCdkPythonApp(
    author_email="csdhong@gmail.com",
    author_name="GenAI",
    cdk_version="2.1.0",
    github=False,
    module_name="src",
    name="src",
    poetry=True,
    python_exec="python",
    version="0.1.0",
)

project.synth()