import yaml
from typing import Dict, List, Any

class LectureParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.metadata: Dict[str, Any] = {}
        self.scenes: List[Dict[str, Any]] = []

    def parse(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
        
        # Split metadata and scenes
        metadata_raw, scenes_raw = content.split('---', 1)
        
        # Parse metadata
        self.metadata = yaml.safe_load(metadata_raw)
        
        # Parse scenes
        scenes_data = yaml.safe_load(scenes_raw)
        
        for scene in scenes_data['scene']:
            scene_type = list(scene.keys())[0]
            scene_content = scene[scene_type]
            
            parsed_scene = {
                'type': scene_type,
                'elements': []
            }
            
            for element in scene_content:
                if isinstance(element, dict):
                    # For structured elements (like the text in intro-scene)
                    parsed_element = element
                else:
                    # For inline elements (like in narration-scene and equation-scene)
                    element_type, content = element.split('->')
                    parsed_element = {
                        'type': element_type.strip()
                    }
                    # Split the attributes and content
                    attributes, content = content.strip().rsplit(',', 1) if ',' in content else ('', content)
                    
                    # Parse attributes
                    for attr in attributes.split(','):
                        if ':' in attr:
                            key, value = attr.split(':', 1)
                            parsed_element[key.strip()] = value.strip()
                    
                    parsed_element['content'] = content.strip()
                
                parsed_scene['elements'].append(parsed_element)
            
            self.scenes.append(parsed_scene)

    def get_metadata(self) -> Dict[str, Any]:
        return self.metadata

    def get_scenes(self) -> List[Dict[str, Any]]:
        return self.scenes

# Example usage
if __name__ == "__main__":
    parser = LectureParser("./lecture/test.lecture")
    parser.parse()
    print("Metadata:", parser.get_metadata())
    print("Scenes:", parser.get_scenes())