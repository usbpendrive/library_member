{
    'name': 'Library Members and Borrowing',
    'description': 'Use library cards for people to borrow books.',
    'author': 'Fernando',
    'depends': ['library_app', 'mail'],
    'license': 'LGPL-3',
    'application': False,
    'data': [
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/member_view.xml',
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/book_list_template.xml',
    ],
}
