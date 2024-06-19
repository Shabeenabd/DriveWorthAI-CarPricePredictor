from flask import Flask,render_template,request,jsonify
import pickle,numpy as np,datetime,os,sys
from app_config import url


script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
model_path=os.path.join(script_directory,'saved_model.pkl')
data=pickle.load(open(model_path,'rb'))
data=pickle.load(open(r'artifact\saved_model.pkl','rb'))
brands=data['brands']
model=data['model']
scaler=data['scaler']

features=model.feature_names_in_

def model_predict(form):
    x=np.zeros(features.shape)
    car,year,kms,owner,fuel=form[1],form[2],form[3],form[4],form[5]
    age=datetime.date.today().year-int(year)
    x[:2]=scaler.transform(np.expand_dims([kms,age],0))
    car_pos=np.where(features=='car_'+car)[0][0] if  'car_'+car in features else -1
    own_pos=np.where(features=='ownership_'+owner)[0][0] if  'ownership_'+owner in features else -1
    fuel_pos=np.where(features=='fuel_type_'+fuel)[0][0] if  'fuel_type_'+fuel in features else -1
    for i in [car_pos,own_pos,fuel_pos]:
        if i>0:
            x[i]=1
    price=np.exp(model.predict(x[np.newaxis,...]))
    return list(price)

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html',data=brands,url=url)

@app.route('/predict',methods=['POST'])
def predict():
    form=list(request.form.values())
    result=model_predict(form)
    return result


# if __name__=="__main__":
#     app.run()

