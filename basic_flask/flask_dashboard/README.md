I found three different ways to integrate Dash with Flask:
1- One proposed by [Todd Birchard](https://hackersandslackers.com/plotly-dash-with-flask/)
2- Another by [Oleg Komarov](https://medium.com/@olegkomarov_77860/how-to-embed-a-dash-app-into-an-existing-flask-app-ea05d7a2210b)
3- And at last another one made up by [Steve Kiefer](https://towardsdatascience.com/embed-multiple-dash-apps-in-flask-with-microsoft-authenticatio-44b734f74532).

Only with the last alternative was it possible for me to keep the Flask-app navbar visible with all the functionalities provided by Flask-login. The backend logic is pretty simple (the dash is stored in a url, which is passed later to Flask route/view as a variable to be loaded using Jinja in an Iframe src).
