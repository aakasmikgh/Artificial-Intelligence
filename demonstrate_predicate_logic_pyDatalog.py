import pyDatalog.pyDatalog as pd
pd.create_terms('father,mother,brother,spouse,grandfather,uncle,X,Y,Z')
 
#Facts
+father('Dashrath','Ram')
+father('Dashrath','Laxman')
+mother('Kaushalya','Ram')
+mother('Kaushalya','Laxman')
+father('Ram','Luv')
+father('Ram','Kush')
+mother('Sita','Luv')
+mother('Sita','Kush')
 
#Rules
grandfather(X,Y) <= father(X,Z) & father(Z,Y)
spouse(X,Y) <= mother(X,Z) & father(Y,Z)
brother(X,Y) <= father(Z,X) & father(Z,Y)
uncle(X,Y) <= father(Z,Y) & brother(X,Z)
 
#Query
grandfather(X,'Luv')
print("Grandfather of Luv is:",X.data[0])
spouse(X, 'Ram')
print("Spouse of Ram is:",X.data[0])
brother(X,'Luv')
print("Brother of Luv is:",X.data[0])
uncle(X,'Luv')
print("Uncle of Luv is:",X.data[0])