from sys import argv
from os import listdir, mkdir
from os.path import exists
import re

SVG_DIRECTORY = argv[1]
DESTINATION = "./" if len(argv) < 3 else argv[2]
APPEND = False if len(argv) < 4 else argv[3] == "append"


def getFiles(path):
    all_files = listdir(path)
    svg_files = []
    for file in all_files:
        if file.split(".")[1] == "svg":
            svg_files.append(file)
    return svg_files


def getNames(files):
    pure = []
    for name in files:
        pure.append(name[0: len(name) - 4])
    return pure


def getSVGPaths(files):
    svgs = []
    for file in files:
        with open(SVG_DIRECTORY + "/" + file) as f:
            path = f.read()
            svgs.append(path[60: len(path) - 6])
    return svgs


def createJSON(svg_path):
    files = getFiles(svg_path)
    names = getNames(files)
    paths = getSVGPaths(files)
    json = "{\n" if APPEND == False else "\t},\n"
    for i in range(0, len(names)):
        json += "\t\"" + names[i] + "\": {\n\t\t\"content\": \"" + paths[i].replace("\"",
                                                                                    "'") + "\",\n\t\t\"viewBox\": \"0 0 20 20\"\n\t}"
        if i != len(names) - 1:
            json += ",\n"
    return json + "\n}"


def saveJSONToFile(svg_path):
    if APPEND:
        with open(DESTINATION + "/lib/icons/util/icons.json", "r+") as file:
            json = "".join(file.readlines()[:-2])
            json += createJSON(svg_path)
            file.seek(0)
            file.write(json)
    else:
        with open(DESTINATION + "/lib/icons/util/icons.json", "w") as file:
            file.write(createJSON(svg_path))
    print("created json file")


def svelteTemplate(name):
    return """<script lang=\"ts\">
    import Icon from \"$lib/icons/util/Icon.svelte\";

    export let size: string = \"1\";
    export let direction: string = \"0\";
    export let className: string = \"\";
    export let color: string = \"black\";
    export let hover: string = \"\";
    export let rotationSpeed: string = \"0\";
    export let backgroundColor: string = \"inherit\";

</script>

<div>
    <Icon 
        name=%s
        size={size}
        direction={direction}
        className={className}
        color={color}
        hover={hover}
        rotationSpeed={rotationSpeed}
        backgroundColor={backgroundColor}
    />
</div>""" % name


def generateSvelteComponents():
    print("creating svelte components...", end=" ")
    for name in getNames(getFiles(SVG_DIRECTORY)):
        name_components = re.split("[-\s]", name)
        svelteName = ""
        for component in name_components:
            svelteName += component.capitalize()
        svelteName += ".svelte"
        with open(DESTINATION + "/lib/icons/components/" + svelteName, "w") as file:
            file.write(svelteTemplate(name))
    print("done")


def generateIcon():
    icon = """<!-- 
How to use this component: 
<Icon name=\"add-outline\" size=\"2\" rotation=\"45\" /> 

name: file name of icon in \"src/icons\"
size: icon size in rem
direction: icon direction in degree
className: css classes
color: icon base color
hover: icon hover color
rotationSpeed: speed of rotation in degrees per second, positive value clockwise, negativ value counterclockwise
-->

<script lang=\"ts\">
    import icons from \"$lib/icons/util/icons.json\"
    type key = keyof typeof icons;

    export let name: key = \"add-outline\";
    export let size: string = \"1\";
    export let direction: string = \"0\";
    export let className: string = \"\";
    export let color: string = \"black\";
    export let hover: string = \"\";
    export let rotationSpeed: string = \"0\";
    export let backgroundColor: string = \"inherit\";

    let style = \"fill: \" + color;

    let spin = Number(direction);
    const spinning = () => {
        spin = ((spin + 0.01 * Number(rotationSpeed)) % 360);
        direction = spin.toString();
    }
    setInterval(spinning, 10);
</script>

<div style=\"width: {size}rem; height: {size}rem; background-color: {backgroundColor}; border-radius: 50%\">
    <!-- svelte-ignore a11y-mouse-events-have-key-events -->
    <svg 
        viewBox=\"0 0 20 20\" 
        class=\"{className}\" 
        style=\"{style}; transform: rotate({direction}deg);\"
        on:mouseover={() => {style = "fill: \" + (hover == "" ? color : hover)}}
        on:mouseout={() => {style = "fill: \" + color}}
    >
        {@html icons[name].content}
    </svg>
</div>"""
    with open(DESTINATION + "/lib/icons/util/Icon.svelte", "w") as file:
        file.write(icon)
    print("created Icon.svelte")


def createDirectories(destination):
    if not exists(destination + "/lib"):
        mkdir(destination + "/lib")
        print("created " + destination + "lib")
    if not exists(destination + "/lib/icons"):
        mkdir(destination + "/lib/icons")
        print("created " + destination + "lib/icons")
    if not exists(destination + "/lib/icons/util"):
        mkdir(destination + "/lib/icons/util")
        print("created " + destination + "lib/icons/util")
    if not exists(destination + "/lib/icons/components"):
        mkdir(destination + "/lib/icons/components")
        print("created " + destination + "lib/icons/components")


def main():
    if APPEND:
        print("Appending new Icons to existing directory")
    else:
        print("Generating new Icons")
    createDirectories(DESTINATION)
    saveJSONToFile(SVG_DIRECTORY)
    generateSvelteComponents()
    generateIcon()
    print("___________________________________________________\nSuccessfully generated svelte components from svgs.")


if __name__ == "__main__":
    main()
