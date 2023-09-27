#!/usr/bin/env python
# coding: utf-8

# ### Importing necessary Libraries 

# In[65]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import plotly.graph_objs as go
from plotly.offline import iplot


# In[66]:


pd.set_option('display.max_rows',None)


# ### importing youth progress index.CSV data  

# In[67]:


data = pd.read_csv("C:\\Users\\jesro\\Desktop\\Youth Progress Index.csv",encoding='ISO-8859-1')
data.head()


# In[68]:


data.dtypes


# In[69]:


data.isnull().sum()


# ### Creating a copy of dataframe 

# In[70]:


df = data.copy()
df.head()


# In[71]:


df.head()


# In[72]:


df.drop(df[df['Country'] == 'World'].index, inplace = True)


# In[73]:


df.reset_index(drop = True,inplace = True)


# In[74]:


df.rename(columns = {'Youth Progress Index':'YPI_score'}, inplace = True)


# In[75]:


df.head()


# In[76]:


df.info()


# ### Drop null values 

# In[77]:


df.dropna(inplace = True)


# In[78]:


df.info()


# In[79]:


df.describe()


# ### Displaying top countries with SPI score greater than 90 

# In[80]:


top_country = df[df['YPI_score']>90].sort_values(by = ['YPI_score'], ascending = False)
top_country


# In[81]:


top_country[['Country','YPI year','YPI_score']].head(10).reset_index(drop = True)


# ### Displaying the average, minimum and maximum score and categorizing them accordingly 

# In[82]:


df.columns = df.columns.str.replace(' ','_')


# In[83]:


print('Highest YPI score :',df['YPI_score'].max())
print('Lowest YPI score :',df['YPI_score'].min())
print('Average YPI score :',df['YPI_score'].mean())


# ### Since the average SPI score is 62.39 and the highest is 96.56 we can consider 88 as the qualifying score 

# In[84]:


df.isnull().sum()


# In[85]:


fig = px.scatter(df.query("YPI_score>=88"),
                 x = 'Basic_Human_Needs',
                 y = 'YPI_score',
                 size = 'YPI_score',
                 hover_name = 'Country',
                 color = 'Country',
                 title = 'Countries with better Basic Human Needs',
                 log_x = True, size_max = 40)

fig.show()


# ### Singapore , Norway and Austria are the top 3 countries with better basic human needs

# In[86]:


fig = px.scatter(df.query("YPI_score>=89"),
           x = 'Opportunity',
           y = 'YPI_score',
           size = 'YPI_score',
           hover_name = 'Country',
          color = 'Country',
          title = 'Countries with better Opportunity',
          size_max = 30)

fig.show()


# ### ### Norway, Denmark and Sweden are the top 3 countries with better Opportunity 

# In[87]:


fig = px.scatter(df.query("YPI_score>=88"),
           x = 'Nutrition_and_Basic_Medical_Care',
           y = 'YPI_score',
           size = 'YPI_score',
           hover_name = 'Country',
          color = 'Country',
          title = 'Countries with better Nutrition and Basic Medical Care',
          size_max = 30)

fig.show()


# ###  Iceland , Gerrmany and Norway are the top 3 countries with better Nutrition and Basic Medical Care

# In[88]:


fig = px.scatter(df.query("YPI_score>=88"),
           x = 'Water_and_Sanitation',
           y = 'YPI_score',
           size = 'YPI_score',
           hover_name = 'Country',
          color = 'Country',
          title = 'Countries with better Water and Sanitation',
          size_max = 30)

fig.show()


# ###  Norway, Iceland and Finland are the top 3 countries with better Water and Sanitation 

# In[89]:


df.shape


# In[90]:


values = dict(type = 'choropleth',
             locations = df['Country'],
             locationmode = 'country names',
             colorscale = 'Blues',
             z = df['YPI_score'],
             text = df['Country'],
             colorbar = {'title' : 'Youth Progress Index'})
layout = dict(title = 'Youth Progress Index',
             geo = dict(showframe = True,
                       projection = {'type':'natural earth'}))

figure = go.Figure(data = [values], layout = layout)
iplot(figure)


# ### A visualization to analyze the overall Youth Progress Index scores globally using a choropleth map: 

# In[91]:


df.head()


# In[92]:


poor_ypi_score_2020 = df[(df.YPI_score<= 60) & (df.YPI_year == 2020)].sort_values(by = 'YPI_score',ascending = True).reset_index(drop = True)
poor_ypi_score_2019 = df[(df.YPI_score<= 60) & (df.YPI_year == 2019)].sort_values(by = 'YPI_score',ascending = True).reset_index(drop = True)


# In[93]:


fig2020 = px.scatter(poor_ypi_score_2020.query("Basic_Human_Needs<=60"),
           x = 'Basic_Human_Needs',
           y = 'Nutrition_and_Basic_Medical_Care',
        color = 'Country',
        size = 'Basic_Human_Needs',
        size_max = 20,
          title = 'Countries with poor Basic Human Needs and Basic Medical Care in the Year 2020')

fig2019 = px.scatter(poor_ypi_score_2019.query("Basic_Human_Needs<=60"),
           x = 'Basic_Human_Needs',
           y = 'Nutrition_and_Basic_Medical_Care',
        color = 'Country',
        size = 'Basic_Human_Needs',
        size_max = 20,
          title = 'Countries with poor Basic Human Needs and Basic Medical Care in the Year 2019')


# In[94]:


fig2019.show(),fig2020.show()


# In[95]:


df.columns


# In[96]:


avg_human_needs = df[['Nutrition_and_Basic_Medical_Care', 'Water_and_Sanitation', 'Shelter',
       'Personal_Safety', 'Access_to_Basic_Knowledge',
       'Access_to_Information_and_Communications', 'Health_and_Wellness',
       'Environmental_Quality', 'Personal_Rights',
       'Personal_Freedom_and_Choice', 'Inclusiveness',
       'Access_to_Advanced_Education']].mean()
avg_human_needs = avg_human_needs.sort_values(ascending = False)


# ### Average Human needs based on several columns 

# In[97]:


avg_human_needs


# In[98]:


fig = px.bar(avg_human_needs,
             y = avg_human_needs.index, 
             x = avg_human_needs.values,
            color = avg_human_needs.index,
            width = 1000, height = 500,
            orientation = 'h',
            title = 'World Average Score for the Past 10 Years ')
fig.update_xaxes(tickangle = -90)
fig.update_traces(texttemplate = '%{x}')
fig.show()


# ### Creating several dataframes based on countries  names and assigning them to its regions name 

# In[99]:


europe_countries = df[df['Country'].isin(['Albania','Andorra','Austria',
                       'Belarus','Belgium','Bosnia and Herzegovina',
                       'Bulgaria','Croatia','Cyprus','Czechia','Czech Republic',
                       'Denmark','Estonia','Finland','France',
                       'Germany','Greece','Gibraltar','Guernsey','Hungary',
                       'Iceland','Ireland','Italy','Isle of Man','Jersey',
                       'Kosovo','Latvia','Liechtenstein','Lithuania',
                       'Luxembourg','Malta','Moldova','Monaco','Montenegro','Macedonia'
                       'Netherlands','Republic of North Macedonia','Norway','Poland',
                       'Portugal','Romania','Russia','San Marino','Serbia',
                        'Serbia and Montenegro','Slovakia','Slovenia','Spain','	Serbia and Montenegro'
                        'Sweden','Switzerland','Turkey','Ukraine','United Kingdom','Vatican City'])]


# In[100]:


europe_countries = europe_countries.reset_index(drop = True)


# In[101]:


europe_countries.shape


# In[102]:


asian_countries = df[df['Country'].isin(['Afghanistan','Armenia','Azerbaijan','Bahrain','Bangladesh',
'Bhutan','British Indian Ocean Territory','Brunei',
'Cambodia','China','Christmas Island','Cocos Islands',
'Hong Kong','India','Indonesia','Iran','Iraq',
'Israel','Japan','Jordan','Kazakhstan','Kuwait','Kyrgyzstan',
'Laos','Lebanon','Macao','Malaysia','Maldives','Mongolia',
'Myanmar','Nepal','North Korea','Oman','Pakistan','Palestinian Territory','Palestine','Russia',
'Philippines','Qatar','Saudi Arabia','United Arab Emirates','Singapore','South Korea','Sri Lanka',
'Syria','Taiwan','Tajikistan','Thailand','Turkey','Timor-Leste','Turkmenistan','United Arab Emirates',
'Uzbekistan','Vietnam','West Bank and Gaza','Yemen'])]


# In[103]:


asian_countries = asian_countries.reset_index(drop = True)
asian_countries.shape


# In[104]:


N_america_countries = df[df['Country'].isin(['Anguilla','Antigua and Barbuda','Aruba','Bahamas','Barbados',
'Belize','Bermuda','British Virgin Islands','Canada','Cayman Islands','Costa Rica','Cuba','Dominica','Dominican Republic',
'El Salvador','Greenland','Grenada','Guadeloupe','Georgia','Guatemala','Haiti','Honduras','Jamaica','Martinique','Mexico','Montserrat',
'Netherlands Antilles','Nicaragua','Panama','Puerto Rico','Saint Barthélemy','Saint Kitts and Nevis','Saint Lucia',
'Saint Martin','Saint Pierre and Miquelon','Saint Vincent and the Grenadines','Trinidad and Tobago',
'Turks and Caicos Islands','U.S. Virgin Islands','United States'])]
N_america_countries = N_america_countries.reset_index(drop = True)
N_america_countries.shape


# In[105]:


S_america_countries = df[df['Country'].isin(['Argentina','Bolivia','Brazil','Chile','Colombia',
                                            'Ecuador','Guyana','Paraguay','Peru','Suriname','Uruguay','Venezuela'])]
S_america_countries = S_america_countries.reset_index(drop = True)


# In[106]:


Aus_countries = df[df['Country'].isin(['Australia','Fiji','Kiribati','Marshall Islands',
                   'Micronesia','Nauru','New Zealand','Palau','Papua New Guinea',
                   'Samoa','Solomon Islands','Tonga','Tuvalu','Vanuatu'])]


# In[107]:


Aus_countries = Aus_countries.reset_index(drop = True)


# In[108]:


africa_countries = df[df['Country'].isin(['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cabo Verde','Cameroon',
                                          'Central African Republic','Chad','Comoros','Congo','Eswatini',"Democratic Republic of','Congo", 
                                          "Republic of the Cote d'Ivoire",'Djibouti','Dominican Republic','Egypt','Guinea',
                                          'Eritrea','Eswatini','Ethiopia','Gabon','Gambia','Ghana','Guinea',
                                          'Guinea-Bissau','Kenya','Lesotho','Liberia','Libya','Lesotho','Madagascar','Malawi','Mali',
                                          'Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria',
                                          'Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone','Somalia',
                                          'South Africa','South Sudan','Sudan','Tanzania','Togo','Tunisia','Trinidad and Tobago','Uganda','Zambia',
                                          'Zimbabwe'])]


# In[109]:


africa_countries = africa_countries.reset_index(drop = True)


# In[110]:


europe_countries.shape


# In[111]:


asian_countries.shape


# In[112]:


N_america_countries.shape


# In[113]:


S_america_countries.shape


# In[114]:


Aus_countries.shape


# In[115]:


africa_countries.shape


# In[116]:


df = df.replace({"Congo, Democratic Republic of": "Democratic Republic of the Congo",
            "Congo, Republic of":"Republic of the Congo",
            "Côte d'Ivoire":"Republic of the Cote d'Ivoire",
            "Gambia, The":"The Gambia",
            "Korea, Republic of":"South Korea"})


# In[117]:


europe_countries.columns


# In[118]:


eu_avg = europe_countries[['Nutrition_and_Basic_Medical_Care', 'Water_and_Sanitation', 'Shelter',
       'Personal_Safety', 'Access_to_Basic_Knowledge',
       'Access_to_Information_and_Communications', 'Health_and_Wellness',
       'Environmental_Quality', 'Personal_Rights',
       'Personal_Freedom_and_Choice', 'Inclusiveness',
       'Access_to_Advanced_Education']].mean()
asia_avg = asian_countries[['Nutrition_and_Basic_Medical_Care', 'Water_and_Sanitation', 'Shelter',
       'Personal_Safety', 'Access_to_Basic_Knowledge',
       'Access_to_Information_and_Communications', 'Health_and_Wellness',
       'Environmental_Quality', 'Personal_Rights',
       'Personal_Freedom_and_Choice', 'Inclusiveness',
       'Access_to_Advanced_Education']].mean()
N_am_avg = N_america_countries[['Nutrition_and_Basic_Medical_Care', 'Water_and_Sanitation', 'Shelter',
       'Personal_Safety', 'Access_to_Basic_Knowledge',
       'Access_to_Information_and_Communications', 'Health_and_Wellness',
       'Environmental_Quality', 'Personal_Rights',
       'Personal_Freedom_and_Choice', 'Inclusiveness',
       'Access_to_Advanced_Education']].mean()
S_am_avg = S_america_countries[['Nutrition_and_Basic_Medical_Care', 'Water_and_Sanitation', 'Shelter',
       'Personal_Safety', 'Access_to_Basic_Knowledge',
       'Access_to_Information_and_Communications', 'Health_and_Wellness',
       'Environmental_Quality', 'Personal_Rights',
       'Personal_Freedom_and_Choice', 'Inclusiveness',
       'Access_to_Advanced_Education']].mean()
aus_avg = Aus_countries[['Nutrition_and_Basic_Medical_Care', 'Water_and_Sanitation', 'Shelter',
       'Personal_Safety', 'Access_to_Basic_Knowledge',
       'Access_to_Information_and_Communications', 'Health_and_Wellness',
       'Environmental_Quality', 'Personal_Rights',
       'Personal_Freedom_and_Choice', 'Inclusiveness',
       'Access_to_Advanced_Education']].mean()
africa_avg = africa_countries[['Nutrition_and_Basic_Medical_Care', 'Water_and_Sanitation', 'Shelter',
       'Personal_Safety', 'Access_to_Basic_Knowledge',
       'Access_to_Information_and_Communications', 'Health_and_Wellness',
       'Environmental_Quality', 'Personal_Rights',
       'Personal_Freedom_and_Choice', 'Inclusiveness',
       'Access_to_Advanced_Education']].mean()


# In[119]:


eu_avg = eu_avg.sort_values(ascending = True)
asia_avg = asia_avg.sort_values(ascending = True)
N_am_avg = N_am_avg.sort_values(ascending = True)
S_am_avg = S_am_avg.sort_values(ascending = True)
aus_avg = aus_avg.sort_values(ascending = True)
africa_avg = africa_avg.sort_values(ascending = True)


# In[120]:


fig = px.bar(eu_avg,
             y = eu_avg.index, 
             x = eu_avg.values,
             width = 650, height = 450,
             color = eu_avg,
            title = 'Europe region Average Score for the Past 10 Years')
fig.update_traces(texttemplate = '%{x}')

fig1 = px.bar(asia_avg,
             y = asia_avg.index, 
             x = asia_avg.values,
              width = 650, height = 450,
             color = eu_avg,
            title = 'Asia region Average Score for the Past 10 Years')
fig1.update_traces(texttemplate = '%{x}')

fig2 = px.bar(N_am_avg,
             y = N_am_avg.index, 
             x = N_am_avg.values,
             width = 650, height = 450,
             color = eu_avg,
            title = 'North American region Average Score for the Past 10 Years')
fig2.update_traces(texttemplate = '%{x}')

fig3 = px.bar(S_am_avg,
             y = S_am_avg.index, 
             x = S_am_avg.values,
             width = 650, height = 450,
             color = eu_avg,
            title = 'South American region Average Score for the Past 10 Years')
fig3.update_traces(texttemplate = '%{x}')

fig4 = px.bar(aus_avg,
             y = aus_avg.index, 
             x = aus_avg.values,
               width = 650, height = 450,
             color = eu_avg,
            title = 'Oceania region Average Score for the Past 10 Years')
fig4.update_traces(texttemplate = '%{x}')

fig5 = px.bar(africa_avg,
             y = africa_avg.index, 
             x = africa_avg.values,
               width = 650, height = 450,
             color = eu_avg,
            title = 'African region Average Score for the Past 10 Years')
fig5.update_traces(texttemplate = '%{x}')

fig5.show(),fig1.show(),fig3.show(),fig2.show(),fig.show(),fig4.show()


# ### Average Score based on several factors for the Past 10 years in the African, Asian, North American, South American, Europe and Oceania Region 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




