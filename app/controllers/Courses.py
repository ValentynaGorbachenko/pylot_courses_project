"""
    Controller File
    Course
"""
from system.core.controller import *
import datetime

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)

        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        courses = self.models['Course'].get_all_courses()
        
        return self.load_view('index.html', courses = courses)

    def add(self):
        valid = True
        user_data = request.form
        if len(user_data['name'])<1:
            flash('Name of the course cannot be empty!')
            valid = False
        elif len(user_data['name']) <15:
            flash('Name of the course cannot be less than 15 characters!')
            valid = False
        if valid:
            added = self.models['Course'].add_course(user_data)
            if not added:
                flash('Something went wrong, please try add a course again!')
            else:
                flash('A new course was added successfully!')
            return redirect('/')
        else:
            return redirect('/')

    def destroy(self, course_id):
        course = self.models['Course'].get_course_by_id(course_id)
        return self.load_view('destroy.html', course = course[0])

    def process_delete(self, course_id):
        print request.form
        print course_id
        if (request.form['submit'] == 'Yes! I want to delete this'):
            deleted = self.models['Course'].delete_course(course_id)
            if deleted:
                flash('You successfully deleted the course!')
                return redirect('/')
            else:
                flash('Something went wrong, please try delete a course again!')
                return redirect('/destroy/'+str(course_id))
        elif (request.form['submit'] == 'No'):
            flash('You changed you mind!')
            return redirect('/')

    def process_update(self, course_id):
        valid = True
        user_data = request.form
        if len(user_data['name'])<1:
            flash('Name of the course cannot be empty!')
            valid = False
        elif len(user_data['name']) <15:
            flash('Name of the course cannot be less than 15 characters!')
            valid = False
        if valid:
            updated = self.models['Course'].update_course(user_data)
            if updated:
                flash('Course was updated successfully!')
                return redirect('/')
            else:
                flash('Something went wrong while updating the course info')
                
        else:
            return redirect('/edit/'+str(course_id))
    
    def edit(self, course_id):
        course = self.models['Course'].get_course_by_id(course_id)
        return self.load_view('update.html', course = course[0])
