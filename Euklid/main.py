from parser.lecture_parser import LectureParser
from scenes.intro import IntroScene
from scenes.narration import NarrationScene
from scenes.equation import EquationScene

def main(lecture_file):
    parser = LectureParser(lecture_file)
    parser.parse()
    
    metadata = parser.get_metadata()
    scenes = parser.get_scenes()
    print(metadata)
    for scene in scenes:
        if scene['type'] == 'intro-scene':
            intro = IntroScene(metadata['title']).construct()
        elif scene['type'] == 'narration-scene':
            NarrationScene([elem for elem in scene['elements'] if elem['type'].startswith('type: text')]).construct()
        elif scene['type'] == 'equation-scene':
            equation = next(elem['content'] for elem in scene['elements'] if elem['type'] == 'type: equation')
            EquationScene(equation).construct()

if __name__ == "__main__":
    main("./lecture/test.lecture")