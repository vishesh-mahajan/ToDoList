import streamlit as st

# Title of the application
st.title('Simple To-Do List')

# Initialize an empty list to store tasks
tasks = []

# Input field to add new task
new_task = st.text_input('Enter new task:')

# Button to add new task to the list
if st.button('Add Task'):
    if new_task:
        tasks.append(new_task)
        st.success(f'Task "{new_task}" added!')
    else:
        st.warning('Please enter a task.')

# Display current tasks
if tasks:
    st.write('### Your To-Do List:')
    for i, task in enumerate(tasks, start=1):
        st.write(f'{i}. {task}')

# Checkbox to remove a task
task_to_remove = st.selectbox('Select task to remove:', options=tasks)
if st.button('Remove Task'):
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        st.success(f'Task "{task_to_remove}" removed!')
    else:
        st.warning('Task not found in the list.')
