{
    'name': 'Odoo Studio',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Visual builder for Odoo customizations',
    'description': """
        Odoo Studio Module
        ==================
        Visual interface for customizing Odoo without coding
    """,
    'depends': ['base', 'web'],
    'data': [
        'security/studio_security.xml',
        'security/ir.model.access.csv',
        'views/field/studio_field_views.xml',
        'views/view/studio_view_views.xml',
        'views/api/studio_api_views.xml',
        'views/api/provider_views.xml',
        'views/studio_menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'studio/static/src/js/studio.js',
            'studio/static/src/js/components/**/*.js',
            'studio/static/src/xml/**/*.xml',
        ],
    },
    'installable': True,
    'application': True,
}