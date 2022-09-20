from setuptools import setup


setup(
    name='cldfbench_tsezacp',
    py_modules=['cldfbench_tsezacp'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'tsezacp=cldfbench_tsezacp:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
        'pyigt',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
