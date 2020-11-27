import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
def generate_launch_description():
    
    config = os.path.join(get_package_share_directory('test_a'),'config','spot_list.yaml')
    
    return LaunchDescription([ 
    
    Node(
        package = 'test_a',
        name = 'move_to_spot',
        node_executable = 'go',
        parameters = [{'spot_name':"table"},
                      {'use_sim_time':False},
                        config],
        output = 'screen',
    )
    ])