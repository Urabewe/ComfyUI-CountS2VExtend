"""
ComfyUI Count Video Extend S2V Node

A utility node that counts active Video S2V Extend nodes in the workflow
and returns count + 1 for use in batch processing or sequencing.
"""

import random

class CountVideoExtendS2VNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"}
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("count_plus_one",)
    FUNCTION = "count_nodes"
    CATEGORY = "Count S2V Extend Nodes"
    
    # This should help with display
    OUTPUT_NODE = True
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        # Always return a different value to force re-execution
        return random.randint(1, 999999)

    def count_nodes(self, prompt=None, extra_pnginfo=None, **kwargs):
        """
        Count active (non-bypassed) 'Video S2V Extend' nodes in the current workflow.
        Returns count + 1.
        """
        count = 0
        
        try:
            # Method 1: From execution prompt (most reliable for active nodes)
            if prompt is not None:
                print("=== DEBUG: All nodes in prompt ===")
                for node_id, node_data in prompt.items():
                    if isinstance(node_data, dict):
                        class_type = node_data.get("class_type")
                        print(f"Node {node_id}: class_type='{class_type}'")
                        
                        # Look for the actual extend nodes (not our own count node)
                        if class_type == "WanSoundImageToVideoExtend":
                            count += 1
                        # Also check for other possible extend node names
                        elif class_type and "VideoExtend" in class_type and "Count" not in class_type:
                            print(f"*** Found video extend node: {class_type} ***")
                            count += 1
                print(f"=== Found {count} matching nodes ===")
            
            # Method 2: Fallback to workflow metadata if prompt unavailable
            elif extra_pnginfo is not None and "workflow" in extra_pnginfo:
                workflow = extra_pnginfo["workflow"]
                if "nodes" in workflow:
                    print("=== DEBUG: All nodes in workflow ===")
                    for node in workflow["nodes"]:
                        if isinstance(node, dict):
                            node_type = node.get("type")
                            print(f"Node type: {node_type}")
                            if node_type == "Video S2V Extend":
                                # Check if node is bypassed (mode 4 = bypassed)
                                mode = node.get("mode", 0)
                                if mode != 4:
                                    count += 1
                            # Also check for similar names
                            elif node_type and "S2V" in node_type and "Extend" in node_type:
                                mode = node.get("mode", 0)
                                if mode != 4:
                                    print(f"*** Found similar node: {node_type} ***")
                                    count += 1
        
        except Exception as e:
            print(f"Error counting Video S2V Extend nodes: {e}")
        
        result = count + 1
        print(f"Found {count} active Video S2V Extend nodes, returning {result}")
        
        # Ensure minimum return value of 1
        if result < 1:
            result = 1
            
        return (result,)


NODE_CLASS_MAPPINGS = {
    "CountVideoExtendS2VNode": CountVideoExtendS2VNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CountVideoExtendS2VNode": "Count Video Extend S2V"
}