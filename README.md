# **Google-Trends-Analyzer**

A Python script that scrapes and analyzes data using Google Trends and various Python libraries.

## 📥 Installation Guide

### Step 1 : Clone the Repository

Clone the repository using the following command.

```
$ git clone https://github.com/sbeen1840/Google-Trends-Analyzer.git
```

### Step 2 : Install Dependencies

**Note** : It is recommended to use a `conda environment` with `Python 3.6` with this code. Before running the commands in this guide, make sure you activate the environment using `$ source activate <name of the env>`

The use the `requirements.txt` file given in the repository to install the dependencies via `pip`.

```
$ pip install -r requirements.txt
```

### Step 3 : Verify the installation of dependencies

To verify whether `pandas`, `pytrends` and `trend` were installed properly, run the following.

```
$ python
>>> import pandas
>>> import pytrends
>>> import trend
```

If there are no error messages upon importing the above dependencies, it would indicate that the they are correctly installed.

## 🔎 Usage

### Step 1 : Update the keywords in the CSV file.

Suppose you have a CSV file containing keywords up to five in one row

### Step 2 : Change Change the route of csv file.

```
self.address = "C:/Users/sbeen/OneDrive/바탕 화면/keyword_data.csv"
```
### Step 3 : Run the script by typing python `main.py` in the terminal.

### Step 4 : Access the data by visiting `http://localhost:5000` in your web browser.

After running the script, you can access keywords representing the search trend by visiting [http://localhost:5000](http://localhost:5000/) in your web browser. You can also see their search volume, normalized. The data will be presented in the form of  json and sorted in descending order.

## 📑 Execution

`docs/trend_exec.ipynb` describes the execution steps of this program pipeline in detail.

## 📌 Notes

As of `2023/02/10`, the above installation and execution steps are only tested on `Window11`. We will update as soon as we test the installation and execution steps on `Linux` and `MacOS`.

## 👤 Authors

- sbeen1840

## 🏷 License

- This project is licensed under the `MIT License` - see the [LICENSE](notion://www.notion.so/LICENSE) file for details

## 🙏 Acknowledgments

## ✍ References

[1]
