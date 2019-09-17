from setuptools import setup


setup(
    name='wagtail1to2',
    py_modules=['wagtail1to2', 'wagtail1to2_command'],
    entry_points={
        'console_scripts': [
            'wagtail1to2=wagtail1to2_command:main'
        ],
    }
)
