pip install -r requirements.txt
behave -f allure_behave.formatter::AllureFormatter -o ./reports/ --no-skipped --tags @Login ./features