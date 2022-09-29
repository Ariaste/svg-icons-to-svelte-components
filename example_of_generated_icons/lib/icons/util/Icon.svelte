<!-- 
How to use this component: 
<Icon name="add-outline" size="2" rotation="45" /> 

name: file name of icon in "src/icons"
size: icon size in rem
direction: icon direction in degree
className: css classes
color: icon base color
hover: icon hover color
rotationSpeed: speed of rotation in degrees per second, positive value clockwise, negativ value counterclockwise
-->

<script lang="ts">
    import icons from "$lib/icons/util/icons.json"
    type key = keyof typeof icons;

    export let name: key = "add-outline";
    export let size: string = "1";
    export let direction: string = "0";
    export let className: string = "";
    export let color: string = "black";
    export let hover: string = "";
    export let rotationSpeed: string = "0";
    export let backgroundColor: string = "inherit";

    let style = "fill: " + color;

    let spin = Number(direction);
    const spinning = () => {
        spin = ((spin + 0.01 * Number(rotationSpeed)) % 360);
        direction = spin.toString();
    }
    setInterval(spinning, 10);
</script>

<div style="width: {size}rem; height: {size}rem; background-color: {backgroundColor}; border-radius: 50%">
    <!-- svelte-ignore a11y-mouse-events-have-key-events -->
    <svg 
        viewBox="0 0 20 20" 
        class="{className}" 
        style="{style}; transform: rotate({direction}deg);"
        on:mouseover={() => {style = "fill: " + hover}}
        on:mouseout={() => {style = "fill: " + color}}
    >
        {@html icons[name].content}
    </svg>
</div>