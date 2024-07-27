from django.shortcuts import render
import pandas as pd
# Create your views here.
def titanic_analysis(request):
    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

    analysis = {
        'total_passengers': df.shape[0],
        'survival_rate': df['Survived'].mean() * 100,
        'average_age': df['Age'].mean(),
        'class_distribution': df['Pclass'].value_counts().to_dict(),
        'embarked_distribution': df['Embarked'].value_counts().to_dict()
    }

    return render(request, 'titanic_analysis.html', {'analysis': analysis})
