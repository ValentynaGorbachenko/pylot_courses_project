""" 
    Model File
    Course
"""
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM courses ORDER BY courses.id DESC")


    def add_course(self, course):
        query = "INSERT INTO courses (title, description, created_at, updated_at) VALUES (:name, :description, NOW(), NOW())"
        data = { 'name': course['name'], 'description': course['description'] }
        self.db.query_db(query, data)
        return True

    def get_course_by_id(self, course_id):
        query = "SELECT * FROM courses WHERE id = :course_id"
        data = { 'course_id': course_id}
        return self.db.query_db(query, data)

    def delete_course(self, course_id):
        query = "DELETE FROM courses WHERE id = :course_id"
        data = { "course_id": course_id }
        self.db.query_db(query, data)
        return True

    def update_course(self, updated_info):
      query = "UPDATE courses SET title=:name, description=:description, updated_at = NOW() WHERE id = :course_id"
      data = { 'name': updated_info['name'], 'description': updated_info['description'], 'course_id': updated_info['course_id']}
      self.db.query_db(query, data)
      return True
