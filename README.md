# Phlask Admin

### Features
- Flask Firebase CRUD Dashboard: Allows developers to easily view, update, delete, and sort/filter for taps

- Phlask Firebase Module: Contains a set of python functions to make complex queries simpler with Firebases RTDB 

- AWS Lambda Function Code Snippet: The code snippet is utilized for the AWS lambda function to make daily updates to the Beta & Test databases

### How to run web app
1. Start up terminal and CD in the dashboard directory
2. Then run the following script

```terminal
flask run
```
For auto-reload when developing use the following:
```terminal
flask --app app.py --debug run
```

For faster development uncomment the top block and comment out the bottom in app.py
####app.py　

```python
@dashboard.route("/")
def main():
    try:
#Static 4 taps for testing
        # water_prod_1=prod.get_tap(water_prod, 1)
        # water_prod_2=prod.get_tap(water_prod, 2)
        # water_prod_3=prod.get_tap(water_prod, 3)
        # water_prod_4=prod.get_tap(water_prod, 4)
        # taps = [water_prod_1, water_prod_2, water_prod_3, water_prod_4]
#------------------------------------------------------------------------------#
# All taps for development
        taps=[]
        db_count = prod.get_count(water_prod)
        for i in range(0, db_count):
            taps_i = prod.get_tap(water_prod, i)
            taps.append(taps_i)

        return render_template("index.html", taps=taps)
    except:
        #if tapnum is not found in database on  /test
        pass
    # return render_template("test.html")
```
