import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt


st.text('This is some text.')

st.markdown('Streamlit is **_really_ cool**.')

st.caption('This is a string that explains something above.')

st.write('Hello, *World!* :sunglasses:')

st.write(1234)

st.write(pd.DataFrame({
 'first column': [1, 2, 3, 4],
'second column': [10, 20, 30, 40],
}))

st.write('1 + 1 = ', 2)


df = pd.DataFrame(np.random.randn(200, 3),columns=['a', 'b', 'c'])

c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)
df = pd.DataFrame(np.random.randn(50, 20),columns=('col %d' % i for i in range(20)))
st.dataframe(df)


#st.dataframe(数据，宽度，高度)
st.dataframe(df, 200, 100)

#DataFrame 加亮
df = pd.DataFrame(np.random.randn(10, 20),columns=('col %d' % i for i in range(20)))
st.dataframe(df.style.highlight_max(axis=0))

#table静态表
df = pd.DataFrame(np.random.randn(10, 5),columns=('col %d' % i for i in range(5)))
st.table(df)

#json
st.json({
     'foo': 'bar',
    'baz': 'boz',
    'stuff': [
                'stuff 1',
                'stuff 2',
                 'stuff 3',
                 'stuff 5',
            ],
})

#折线图
chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])

st._arrow_line_chart(chart_data)

#面积图
chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
st.area_chart(chart_data)

#条形图
chart_data = pd.DataFrame(np.random.randn(50, 3),columns=['a', 'b', 'c'])
st.bar_chart(chart_data)

#柱状图
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.pyplot(fig)





#实例：积分柱状图
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_excel('jifen.xlsx')
st.dataframe(df)#打出表格

options = st.multiselect('你选哪一年？？？', df['年份'].unique())
st.write('You selected:', options)
new_df = df['年份']
st.dataframe(new_df)#打出表格

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
x=df['年份']
print(x)
y=df['及格线']
print(y)
z=df['noting to do']
print(z)
w=df['work']
print(w)
q=df['work and shui']
print(q)
# 设置图框的大小
fig = plt.figure(figsize=(10,6))
# 绘图，做折线图
plt.plot(x,#x轴
         y,#y轴
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = 'steelblue', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='steelblue', # 点的填充色
         label='及格线'#标签
         )
plt.plot(x,#x轴
         z,#y轴
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#ff9999', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='#ff9999', # 点的填充色
         label='nothing'#标签
         )
plt.plot(x,#x轴
         w,#y轴
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#8c564b', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='#8c564b', # 点的填充色
         label='work'#标签
         )
plt.plot(x,#x轴
         q,#y轴
         linestyle = '-', # 折线类型
         linewidth = 2, # 折线宽度
         color = '#bcbd22', # 折线颜色
         marker = 'o', # 点的形状
         markersize = 6, # 点的大小
         markeredgecolor='black', # 点的边框色
         markerfacecolor='#bcbd22', # 点的填充色
         label='work and shui'#标签
         )
# 添加标题和坐标轴标签
plt.title('积分状况折线图')
plt.xlabel('年份')
plt.ylabel('分值')
plt.xticks(rotation = 60)#x轴标签倾斜60度

plt.legend(loc='best',frameon=False)#图例，显示label，去掉边框
#plt.show()
st.pyplot(fig)


#选项
options = st.multiselect( 'What are your favorite colors',  ['Green', 'Yellow', 'Red', 'Blue'], ['Yellow', 'Red'])
st.write('You selected:', options)

#选项 滑块
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

#选项 范围滑块
values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

#选项 范围时间滑块
from datetime import time
appointment = st.slider("Schedule your appointment:",value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

#用复选框隐藏数据
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    chart_data


#用选择框作为选项
option = st.selectbox('Which number do you like best?', df['年份'])
'You selected: ', option


#两次筛选结果 交集
nianfen = st.multiselect('请选择年份', df['年份'].unique())
jigexian = st.multiselect('及格线', df['及格线'].unique())
# Filter dataframe
new_df = df[(df['年份'].isin(nianfen)) & (df['及格线'].isin(jigexian))]
# write dataframe to screen
st.write(new_df)

print('..................')
