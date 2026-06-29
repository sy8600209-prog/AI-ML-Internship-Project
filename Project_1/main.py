import numpy  # for numeric calculation
import pandas as pd # fro csv file handling
from sklearn.model_selection import train_test_split # for training the model
from sklearn.linear_model import LinearRegression  # for prediction model
from sklearn.metrics import r2_score # for model Evaluation

# viwe data function
def view_data():
    df=pd.read_csv("utility_data.csv")
    print(df)
    
    
# add data function  
def add_data(df):
    try:
        days=int(input("Enter the  number of days:"))
        family_member=int(input("Enter the number of Family Members:"))
        PreviousUsage=int(input("Enter the Previous Usage:"))
        CurrentUsage=int(input("Enter the Current Usage:"))
        new_data={
            "Days":days,
            "FamilyMembers":family_member,
            "PreviousUsage":PreviousUsage,
            "CurrentUsage":CurrentUsage
        }
    except ValueError:
        print("====Enter only Number====")
    else:
        df.loc[len(df)]=new_data
        df.to_csv("utility_data.csv",index=False)
        print("Data Added Successfully")
    
# update data function  
def update_data(df):
    print(df)
    while True:
        try:
            row=int(input("Enter the row number(Row number start with 0):"))
            if(row>=df.shape[0]):
                 print("======Invalid Row Number======")
                 break
        except ValueError:
            print("====Enter only Number====")
            break
        print("==========================")
        print("1.update_days")
        print("2.update Family_member")
        print("3.update PreviousUsage")
        print("4 update CurrentUsage")
        print("5 update All")
        
        try :
             a=int(input("Enter Your Choice: "))
        except ValueError:
                        print("====Enter only Number====")
                        break
         
        else:
            if(a==1):
                try :
                    days=int(input("Enter the  number of days:"))
                    
                except ValueError:
                        print("====Enter only Number====")
                        break
                else:
                    df.loc[row,"Days"]=days
                    df.to_csv("utility_data.csv",index=False)
                    print("Data update Successfully")
                    break        
            elif(a==2):
                try:
                    family_member=int(input("Enter the number of Family Member:"))
                    
                except ValueError:
                        print("====Enter only Number====")
                        break
                else:
                    df.loc[row,"FamilyMembers"]=family_member
                    df.to_csv("utility_data.csv",index=False)
                    print("Data update Successfully")
                    break        
            elif(a==3):
                try:
                    PreviousUsage=int(input("Enter the Previous Usage:"))
                    
                except ValueError:
                        print("====Enter only Number====")
                        break
                else:
                    df.loc[row,"PreviousUsage"]=PreviousUsage
                    df.to_csv("utility_data.csv",index=False)
                    print("Data update Successfully")
                    break        
            elif(a==4):
                try:
                    CurrentUsage=int(input("Enter the Current Usage:"))
                    
                except ValueError:
                        print("====Enter only Number====")
                        break
                else:
                    df.loc[row,"CurrentUsage"]=CurrentUsage
                    df.to_csv("utility_data.csv",index=False)
                    print("Data update Successfully")
                    break        
            elif(a==5):
                try:
                    days=int(input("Enter the  number of days:"))
                    family_member=int(input("Enter the number of Family Member:"))
                    PreviousUsage=int(input("Enter the Previous Usage:"))
                    CurrentUsage=int(input("Enter the Current Usage:"))
                    
                    
                except ValueError:
                        print("====Enter only Number====")

                        break
                else:
                    df.loc[row,"Days"]=days
                    df.loc[row,"FamilyMembers"]=family_member
                    df.loc[row,"PreviousUsage"]=PreviousUsage
                    df.loc[row,"CurrentUsage"]=CurrentUsage
                    df.to_csv("utility_data.csv",index=False)
                    print("Data update Successfully")
                    
                    break        
            else:
                print("Invalid Choice")
        
    
                
    
    
# function for creating a ML model and  to train model
def train_data(df):
    
    x=df.drop("CurrentUsage",axis=1)
    y=df["CurrentUsage"]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    model=LinearRegression()
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    print("R2 score of this model is :",r2_score(y_test,y_pred))
    return model    
    
    
    
# function for prediction through ML model
def predict(model):
    days=int(input("Enter the  number of days:"))
    family_member=int(input("Enter the number of Family Members:"))
    PreviousUsage=int(input("Enter the Previous Usage:"))
    pred=pd.DataFrame([[days,family_member,PreviousUsage]],columns=["Days","FamilyMembers","PreviousUsage"])
    print("======Predicted Data======")
    print(f"Current Usage is:{model.predict(pred)[0]:.2f} units")
   
   
   
# menu -driven console system
def menu():
    while True:
        print("\n====== Utility Usage Prediction Tool======")
        print("1.View Data")
        print("2.Add Data")
        print("3.Update Data")
        print("4.Train Data")
        print("5.Predict Usage")
        print("6.Exit")
        df=pd.read_csv("utility_data.csv")
        try :
             a=int(input("Enter Your Choice: "))
        except ValueError:
                        print("=======Enter only Number======")
         
        else:
            if(a==1):
                view_data()
            elif(a==2):
                add_data(df)
            elif(a==3):
                update_data(df)
            elif(a==4):
                train_data(df)
                print("Model is train successfuly")
            elif(a==5):
                model=train_data(df)
                predict(model)
            elif(a==6):
                print("Thank You!")
                break
            else:
                print("Invalid Choice")
                
                
                
                
menu()# calling main menu function