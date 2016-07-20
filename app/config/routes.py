"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Courses'
routes['POST']['/courses/add'] = 'Courses#add'
routes['/destroy/<int:course_id>'] = 'Courses#destroy'
routes['POST']['/process_delete/<int:course_id>'] = 'Courses#process_delete'
routes['/edit/<int:course_id>'] = 'Courses#edit'
routes['POST']['/process_update/<int:course_id>'] = 'Courses#process_update'

