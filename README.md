### JSONPlaceholder CRUD Operation Testing

- Test scenarios are mentioned [here](test_scenarios.md)
- Automated tests for CRUD operations are present [here](test-cases)
- Test data is managed in a json file [here](resources/test_data.json)

**Test Execution:**

- Execute below command in Terminal to execute all the automated tests present [here](test-cases)
        
        python -m pytest --alluredir="./reportdir"  test-cases/*

- Individual test class can be run with below command:

        python -m pytest --alluredir="./reportdir"  test-cases/{test_class_name}

**Allure Reports:**

- After the test execution is finished an Allure Report would be generated.
  - To view the execution report please execute below command in the Terminal:
        
        allure serve "./reportdir"
  - This will open the HTML report in a browser session
  - It is necessary to clear the [reportdir](reportdir) so that each execution will have it's specific run results, with below command in a Bash terminal:

        rm -rf reportdir/*

**Test Execution Logs:**

- Logging has been implemented in the framework
- With each test run, a logs file would be generated with a unique timestamp [here](execution-logs)
- These logs can be referred later for the debugging purpose