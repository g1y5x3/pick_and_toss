from setuptools import setup

package_name = 'pick_and_toss'
data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch',   ['launch/ur3e_simple_driver_launch.py']))
data_files.append(('share/' + package_name + '/worlds',   ['worlds/ur3e_world.wbt']))
data_files.append(('share/' + package_name + '/resource', ['resource/ur3e_arms_simple.urdf', 'resource/ur3e_cameras.urdf']))
data_files.append(('share/' + package_name, ['package.xml']))

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user.name@mail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_robot_driver = pick_and_toss.my_robot_driver:main',
            'ur3e_driver = pick_and_toss.ur3e_simple_driver:main',
        ],
    },
)

