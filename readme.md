# Website Accessibility Checker

A Python script that checks the accessibility of websites by making HTTP GET requests to the provided URLs.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/wamuyu-felix/website-accessibility-checker.git
   ```

2. Navigate to the project directory:

   ```shell
   cd website-accessibility-checker
   ```

3. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:

   ```shell
   python website_accessibility_checker.py example.com,google.com,youtube.com
   ```

   Replace `example.com,google.com,youtube.com` with your desired comma-separated list of URLs to check.

2. The script will check the accessibility of each URL and provide the result.

## Features

- Validates the format of URLs and adds the "http://" scheme if missing.
- Checks the accessibility of websites by making HTTP GET requests.
- Prints the status of each website, indicating whether it is accessible or not.
- Accessible URLs are shown in green with a checkmark (✓).
- Inaccessible URLs are shown in red with an "x" (✗) and the corresponding status code.

## Dependencies

The script requires the following dependencies:

- requests
- colorama

To install the dependencies, run the following command:

```shell
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

```

Feel free to adjust the content and sections as per your requirements.
```
