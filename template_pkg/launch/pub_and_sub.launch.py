from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='template_pkg',
            executable='publisher',
            output='screen',
            emulate_tty=True
        ),
        Node(
            package='template_pkg',
            executable='subscriber',
            output='screen',
            emulate_tty=True
        )
    ])
