"""
ComfyUI Count Video Extend S2V Node

A utility node that counts active Video S2V Extend nodes in the workflow
and returns count + 1 for use in batch processing or sequencing.
"""

from .count_video_extend_s2v_node import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']