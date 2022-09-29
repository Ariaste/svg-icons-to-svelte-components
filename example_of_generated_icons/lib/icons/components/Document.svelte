<script lang="ts">
    import Icon from "$lib/icons/util/Icon.svelte";

    export let size: string = "1";
    export let direction: string = "0";
    export let className: string = "";
    export let color: string = "black";
    export let hover: string = "";
    export let rotationSpeed: string = "0";
    export let backgroundColor: string = "inherit";

</script>

<div>
    <Icon 
        name=document
        size={size}
        direction={direction}
        className={className}
        color={color}
        hover={hover}
        rotationSpeed={rotationSpeed}
        backgroundColor={backgroundColor}
    />
</div>