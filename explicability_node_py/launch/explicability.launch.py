from launch import LaunchDescription
from llama_bringup.utils import create_llama_launch
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([
        create_llama_launch(
            n_ctx=512,

            n_threads=4,
            n_predict=512,
            n_batch=8,

            model="marcoroni-13b.Q4_0.gguf",

            prefix="\n\n### Instruction:\n",
            suffix="\n\n### Response:\n",
            stop="### Instruction:\n",
        ),

        Node(
            package="explicability_node_py",
            executable="explicability_node",
            name='explicability'
        )
    ])
