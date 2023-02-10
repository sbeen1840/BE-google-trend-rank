# **Google-Trends-Analyzer**

A Python script that scrapes and analyzes data using Google Trends and various Python libraries.
![image](https://user-images.githubusercontent.com/108644811/218132616-bb7c7182-d5a9-4d68-b0f9-b5843c737ad3.png)

# 📥 Installation Guide

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

# 🔎 Usage

### Step 1 : Update the keywords in the CSV file.

|1|2|3|4|5|
|---|---|---|---|---|
|JAVA| java|
|C++| c++|
|PYTHON| python| py| PY|
|javaScript| javascript| JAVASCRITP|

Suppose you have a CSV file containing keywords up to five in one row

### Step 2 : Change Change the route of csv file.

```
self.address = "C:/Users/sbeen/OneDrive/바탕 화면/keyword_data.csv"
```
### Step 3 : Run the script by typing python `main.py` in the terminal.
![image](https://user-images.githubusercontent.com/108644811/218135256-a527b011-0b86-4f49-98ee-83b8b41698b1.png)

### Step 4 : Access the data by visiting `http://localhost:5000` in your web browser.

After running the script, you can access keywords representing the search trend by visiting [http://localhost:5000](http://localhost:5000/) in your web browser. You can also see their search volume, normalized. The data will be presented in the form of  json and sorted in descending order.

# 💡 Results
|Console output|Web json data http://localhost:5000 |
|--|--|
|![](https://velog.velcdn.com/images/sbeen1840/post/ebce6bfb-d833-4f32-bfd8-4010b64fe9d4/image.png)|![image](https://user-images.githubusercontent.com/108644811/218129926-1a4f0d54-57c6-4b75-bcc6-b33929be18c7.png)|


# 📑 Execution

`docs/trend_exec.ipynb` describes the execution steps of this program pipeline in detail.

# 📌 Notes

As of `2023/02/10`, the above installation and execution steps are only tested on `Window11`. We will update as soon as we test the installation and execution steps on `Linux` and `MacOS`.

# 👤 Authors

- sbeen1840

# 🏷 License

- This project is licensed under the `MIT License` - see the [LICENSE](notion://www.notion.so/LICENSE) file for details

# 🙏 Acknowledgments

# ✍ References
