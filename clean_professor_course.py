import pandas as pd

# 读取数据
file_path = 'course2301//Template List-Revised-1102.xlsx'
df = pd.read_excel(file_path)

# 过滤掉 Activity Type 为 Lecture 的数据
lecture_df = df[df['Activity Type'] == 'Lecture']

# 清洗数据，提取教授和课程对应关系，并以分号分隔教授名称
# prof_course_df = lecture_df[['Module Code', 'Course Instructor&New/Part-Time']].copy()
prof_course_df = lecture_df[['Module Code', 'Course Instructor&New/Part-Time']].copy()

# 创建一个新的DataFrame来存储每个教授和课程的对应关系
expanded_df = pd.DataFrame(columns=['Module Code', 'Course Instructor&New/Part-Time'])

# 遍历每一行，将教授列中的多个教授分割成单独的行
for index, row in prof_course_df.iterrows():
    instructors = str(row['Course Instructor&New/Part-Time']).split(';')
    for instructor in instructors:
        expanded_df = expanded_df.append({'Module Code': row['Module Code'], 
                                          'Course Instructor&New/Part-Time': instructor.strip()}, ignore_index=True)

# 删除重复行
expanded_df.drop_duplicates(inplace=True)

# 保存清洗后的数据
expanded_df.to_excel('cleaned_prof_course_data_expanded.xlsx', index=False)

# 查看清洗后的数据
print(expanded_df.head())

