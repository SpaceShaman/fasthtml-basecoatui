"""Generated Basecoat components."""

from typing import Literal

from fasthtml.components import ft_html

BASECOAT_VERSION = '1.2.1'
STYLES = ('luma', 'lyra', 'maia', 'mira', 'nova', 'rhea', 'sera', 'vega')
Style = Literal['luma', 'lyra', 'maia', 'mira', 'nova', 'rhea', 'sera', 'vega']

__all__ = [
    'Accordion',
    'Alert',
    'AlertDialog',
    'Attachment',
    'Avatar',
    'AvatarBadge',
    'AvatarGroup',
    'Badge',
    'Breadcrumb',
    'Bubble',
    'BubbleGroup',
    'Button',
    'ButtonGroup',
    'Card',
    'CardAction',
    'Carousel',
    'Checkbox',
    'CodeBlock',
    'Combobox',
    'ComboboxTriggerIcon',
    'Command',
    'CommandDialog',
    'Dialog',
    'Drawer',
    'DropdownMenu',
    'Empty',
    'Field',
    'Fieldset',
    'Input',
    'InputGroup',
    'InputOtp',
    'Item',
    'ItemGroup',
    'Kbd',
    'Label',
    'Marker',
    'Message',
    'MessageGroup',
    'NativeSelect',
    'Popover',
    'Progress',
    'Radio',
    'Select',
    'Sheet',
    'Sidebar',
    'Skeleton',
    'Slider',
    'Switch',
    'Table',
    'TableContainer',
    'Tabs',
    'Textarea',
    'Toast',
    'ToastContent',
    'Trace',
    'TraceLine',
]


def _option(name: str, value: str, choices: tuple[str, ...]) -> str:
    if value not in choices:
        raise ValueError(f"Invalid {name}: {value!r}; choose from {choices}")
    return value

def Accordion(
    *children,
    cls: str = "",
    tag: str = 'section',
    **attrs,
):
    'Root accordion container. Add data-multiple to allow multiple open items.'
    classes = ' '.join(filter(None, ('accordion', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Alert(
    *children,
    variant: Literal['destructive'] | None = None,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Main container. Use data-variant="destructive" for error states.'
    if variant is not None:
        attrs['data-variant'] = _option('variant', variant, ('destructive',))
    classes = ' '.join(filter(None, ('alert', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def AlertDialog(
    *children,
    cls: str = "",
    tag: str = 'dialog',
    **attrs,
):
    'Native modal dialog. Add aria-labelledby and aria-describedby when title and description are present. Use data-size="sm" for the compact upstream size.'
    classes = ' '.join(filter(None, ('alert-dialog', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Attachment(
    *children,
    orientation: Literal['vertical'] | None = None,
    size: Literal['default', 'sm', 'xs'] | None = None,
    state: Literal['error', 'idle'] | None = None,
    cls: str = "",
    tag: str = 'li',
    **attrs,
):
    'Basecoat Attachment.'
    if orientation is not None:
        attrs['data-orientation'] = _option('orientation', orientation, ('vertical',))
    if size is not None:
        attrs['data-size'] = _option('size', size, ('default', 'sm', 'xs'))
    if state is not None:
        attrs['data-state'] = _option('state', state, ('error', 'idle'))
    classes = ' '.join(filter(None, ('attachment', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Avatar(
    *children,
    size: Literal['lg', 'sm'] | None = None,
    cls: str = "",
    tag: str = 'span',
    **attrs,
):
    'Avatar root. Use it standalone or as a direct child of .avatar-group . Add data-size="sm" or data-size="lg" for alternate sizes.'
    if size is not None:
        attrs['data-size'] = _option('size', size, ('lg', 'sm'))
    classes = ' '.join(filter(None, ('avatar', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def AvatarBadge(
    *children,
    cls: str = "",
    tag: str = 'span',
    **attrs,
):
    'Status badge positioned at the block-end inline-end corner. It can be empty or contain an icon.'
    classes = ' '.join(filter(None, ('avatar-badge', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def AvatarGroup(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Optional parent that groups avatars with overlap.'
    classes = ' '.join(filter(None, ('avatar-group', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Badge(
    *children,
    variant: Literal['destructive', 'ghost', 'link', 'outline', 'primary', 'secondary'] | None = None,
    cls: str = "",
    tag: str = 'span',
    **attrs,
):
    'Basecoat Badge.'
    if variant is not None:
        attrs['data-variant'] = _option('variant', variant, ('destructive', 'ghost', 'link', 'outline', 'primary', 'secondary'))
    classes = ' '.join(filter(None, ('badge', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Breadcrumb(
    *children,
    cls: str = "",
    tag: str = 'nav',
    **attrs,
):
    'Basecoat Breadcrumb.'
    classes = ' '.join(filter(None, ('breadcrumb', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Bubble(
    *children,
    align: Literal['end'] | None = None,
    variant: Literal['default', 'destructive', 'ghost', 'muted', 'outline', 'secondary', 'tinted'] | None = None,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Basecoat Bubble.'
    if align is not None:
        attrs['data-align'] = _option('align', align, ('end',))
    if variant is not None:
        attrs['data-variant'] = _option('variant', variant, ('default', 'destructive', 'ghost', 'muted', 'outline', 'secondary', 'tinted'))
    classes = ' '.join(filter(None, ('bubble', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def BubbleGroup(
    *children,
    cls: str = "",
    tag: str = 'ol',
    **attrs,
):
    'Basecoat BubbleGroup.'
    attrs.setdefault('role', 'list')
    classes = ' '.join(filter(None, ('bubble-group', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Button(
    *children,
    size: Literal['default', 'icon', 'icon-lg', 'icon-sm', 'icon-xs', 'lg', 'sm', 'xs'] | None = None,
    variant: Literal['destructive', 'ghost', 'link', 'outline', 'primary', 'secondary'] | None = None,
    cls: str = "",
    tag: str = 'button',
    **attrs,
):
    'Button root. Use a native <button> for actions and <a> for navigation.'
    if size is not None:
        attrs['data-size'] = _option('size', size, ('default', 'icon', 'icon-lg', 'icon-sm', 'icon-xs', 'lg', 'sm', 'xs'))
    if variant is not None:
        attrs['data-variant'] = _option('variant', variant, ('destructive', 'ghost', 'link', 'outline', 'primary', 'secondary'))
    classes = ' '.join(filter(None, ('btn', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def ButtonGroup(
    *children,
    orientation: Literal['vertical'] | None = None,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Basecoat ButtonGroup.'
    attrs.setdefault('role', 'group')
    if orientation is not None:
        attrs['data-orientation'] = _option('orientation', orientation, ('vertical',))
    classes = ' '.join(filter(None, ('button-group', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Card(
    *children,
    size: Literal['sm'] | None = None,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'The card container. Use data-size="sm" for a denser layout.'
    if size is not None:
        attrs['data-size'] = _option('size', size, ('sm',))
    classes = ' '.join(filter(None, ('card', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def CardAction(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Action or metadata placed in the top-right of the header. Use <menu class="card-action"> when the content is a list of commands.'
    classes = ' '.join(filter(None, ('card-action', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Carousel(
    *children,
    orientation: Literal['vertical'] | None = None,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Basecoat Carousel.'
    attrs.setdefault('role', 'region')
    if orientation is not None:
        attrs['data-orientation'] = _option('orientation', orientation, ('vertical',))
    classes = ' '.join(filter(None, ('carousel', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Checkbox(
    *children,
    cls: str = "",
    tag: str = 'input',
    **attrs,
):
    'Basecoat Checkbox.'
    attrs.setdefault('type', 'checkbox')
    classes = ' '.join(filter(None, ('input', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def CodeBlock(
    *children,
    size: Literal['sm'] | None = None,
    variant: Literal['destructive'] | None = None,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Basecoat CodeBlock.'
    if size is not None:
        attrs['data-size'] = _option('size', size, ('sm',))
    if variant is not None:
        attrs['data-variant'] = _option('variant', variant, ('destructive',))
    classes = ' '.join(filter(None, ('code-block', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Combobox(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Root element. Add data-auto-highlight="true" to make the first visible option active when the list opens or filters. Add data-format="object" to serialize selected values as objects. Add data-filter="manual" when your app owns filtering.'
    classes = ' '.join(filter(None, ('combobox', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def ComboboxTriggerIcon(
    *children,
    cls: str = "",
    tag: str = 'svg',
    **attrs,
):
    'Decorative trailing icon for input-style comboboxes. Replace the SVG to customize the icon.'
    classes = ' '.join(filter(None, ('combobox-trigger-icon', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Command(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Root command menu. Can also be used standalone without the dialog wrapper. Add data-filter="manual" when your app owns filtering, such as remote search or a local Lunr index.'
    classes = ' '.join(filter(None, ('command', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def CommandDialog(
    *children,
    cls: str = "",
    tag: str = 'dialog',
    **attrs,
):
    'Dialog variant. Wraps one direct child <div class="command"> . Add aria-label or aria-labelledby for an accessible name.'
    classes = ' '.join(filter(None, ('command-dialog', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Dialog(
    *children,
    cls: str = "",
    tag: str = 'dialog',
    **attrs,
):
    'Native modal dialog. Add aria-labelledby="{ TITLE_ID }" and aria-describedby="{ DESCRIPTION_ID }" when title and description are present. Add width utilities to the inner <div> when a dialog needs a custom size. The macro also adds backdrop-click close handling.'
    classes = ' '.join(filter(None, ('dialog', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Drawer(
    *children,
    side: Literal['bottom', 'left', 'right', 'top'] | None = None,
    cls: str = "",
    tag: str = 'dialog',
    **attrs,
):
    'Native modal drawer. Omit data-side for the default bottom drawer. Add aria-labelledby and aria-describedby when title and description are present. JavaScript adds the data-drawer-initialized flag and manages animated close behavior.'
    if side is not None:
        attrs['data-side'] = _option('side', side, ('bottom', 'left', 'right', 'top'))
    classes = ' '.join(filter(None, ('drawer', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def DropdownMenu(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Relative wrapper for the trigger and inline menu content.'
    classes = ' '.join(filter(None, ('dropdown-menu', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Empty(
    *children,
    cls: str = "",
    tag: str = 'section',
    **attrs,
):
    'The empty-state container.'
    classes = ' '.join(filter(None, ('empty', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Field(
    *children,
    orientation: Literal['horizontal', 'responsive'] | None = None,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Single field wrapper. Add data-orientation when needed.'
    attrs.setdefault('role', 'group')
    if orientation is not None:
        attrs['data-orientation'] = _option('orientation', orientation, ('horizontal', 'responsive'))
    classes = ' '.join(filter(None, ('field', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Fieldset(
    *children,
    cls: str = "",
    tag: str = 'fieldset',
    **attrs,
):
    'Native group for related fields. Use <legend> for the label and a following <p> for description.'
    classes = ' '.join(filter(None, ('fieldset', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Input(
    *children,
    cls: str = "",
    tag: str = 'input',
    **attrs,
):
    'Basecoat Input.'
    attrs.setdefault('type', 'email')
    classes = ' '.join(filter(None, ('input', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def InputGroup(
    *children,
    orientation: Literal['vertical'] | None = None,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Basecoat InputGroup.'
    if orientation is not None:
        attrs['data-orientation'] = _option('orientation', orientation, ('vertical',))
    classes = ' '.join(filter(None, ('input-group', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def InputOtp(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Basecoat InputOtp.'
    classes = ' '.join(filter(None, ('input-otp', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Item(
    *children,
    size: Literal['default', 'sm', 'xs'] | None = None,
    variant: Literal['default', 'muted', 'outline'] | None = None,
    cls: str = "",
    tag: str = 'article',
    **attrs,
):
    'The item root. Use data-variant="outline|muted" and data-size="sm|xs" when needed.'
    if size is not None:
        attrs['data-size'] = _option('size', size, ('default', 'sm', 'xs'))
    if variant is not None:
        attrs['data-variant'] = _option('variant', variant, ('default', 'muted', 'outline'))
    classes = ' '.join(filter(None, ('item', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def ItemGroup(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Groups related items. Use role="listitem" on child items when they are not native list items.'
    attrs.setdefault('role', 'list')
    classes = ' '.join(filter(None, ('item-group', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Kbd(
    *children,
    cls: str = "",
    tag: str = 'kbd',
    **attrs,
):
    'Basecoat Kbd.'
    classes = ' '.join(filter(None, ('kbd', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Label(
    *children,
    cls: str = "",
    tag: str = 'label',
    **attrs,
):
    'Basecoat Label.'
    classes = ' '.join(filter(None, ('label', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Marker(
    *children,
    variant: Literal['border', 'separator'] | None = None,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Basecoat Marker.'
    if variant is not None:
        attrs['data-variant'] = _option('variant', variant, ('border', 'separator'))
    classes = ' '.join(filter(None, ('marker', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Message(
    *children,
    align: Literal['end'] | None = None,
    cls: str = "",
    tag: str = 'li',
    **attrs,
):
    'Basecoat Message.'
    if align is not None:
        attrs['data-align'] = _option('align', align, ('end',))
    classes = ' '.join(filter(None, ('message', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def MessageGroup(
    *children,
    cls: str = "",
    tag: str = 'ol',
    **attrs,
):
    'Basecoat MessageGroup.'
    attrs.setdefault('role', 'list')
    classes = ' '.join(filter(None, ('message-group', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def NativeSelect(
    *children,
    cls: str = "",
    tag: str = 'select',
    **attrs,
):
    'Basecoat NativeSelect.'
    classes = ' '.join(filter(None, ('select', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Popover(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Relative wrapper for the trigger and inline popover content.'
    classes = ' '.join(filter(None, ('popover', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Progress(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Progress root. Set aria-label or aria-labelledby , plus aria-valuenow , aria-valuemin , and aria-valuemax .'
    attrs.setdefault('role', 'progressbar')
    classes = ' '.join(filter(None, ('progress', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Radio(
    *children,
    cls: str = "",
    tag: str = 'input',
    **attrs,
):
    'Basecoat Radio.'
    attrs.setdefault('type', 'radio')
    classes = ' '.join(filter(None, ('input', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Select(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Select root. Add data-placeholder to show placeholder text when no value is selected. Supports data-close-on-select="true" for multiple select and data-format="object" for serialized object values.'
    classes = ' '.join(filter(None, ('select', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Sheet(
    *children,
    side: Literal['bottom', 'left', 'right', 'top'] | None = None,
    cls: str = "",
    tag: str = 'dialog',
    **attrs,
):
    'Basecoat Sheet.'
    if side is not None:
        attrs['data-side'] = _option('side', side, ('bottom', 'left', 'right', 'top'))
    classes = ' '.join(filter(None, ('sheet', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Sidebar(
    *children,
    side: Literal['left', 'right'] | None = None,
    cls: str = "",
    tag: str = 'aside',
    **attrs,
):
    'Sidebar root. Supports id , data-side="left|right" , data-initial-open="false" , data-initial-mobile-open="true" , and data-breakpoint . JavaScript manages aria-hidden , inert , and the internal data-sidebar-initialized flag.'
    if side is not None:
        attrs['data-side'] = _option('side', side, ('left', 'right'))
    classes = ' '.join(filter(None, ('sidebar', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Skeleton(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Basecoat Skeleton.'
    classes = ' '.join(filter(None, ('skeleton', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Slider(
    *children,
    cls: str = "",
    tag: str = 'input',
    **attrs,
):
    'Native range input styled as a slider. Width utilities such as w-full can be added directly.'
    attrs.setdefault('type', 'range')
    classes = ' '.join(filter(None, ('input', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Switch(
    *children,
    size: Literal['sm'] | None = None,
    cls: str = "",
    tag: str = 'input',
    **attrs,
):
    'The switch control. Use native checkbox state: add checked for an initially enabled switch, disabled for a disabled switch, and aria-invalid="true" for invalid state.'
    attrs.setdefault('role', 'switch')
    attrs.setdefault('type', 'checkbox')
    if size is not None:
        attrs['data-size'] = _option('size', size, ('sm',))
    classes = ' '.join(filter(None, ('input', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Table(
    *children,
    cls: str = "",
    tag: str = 'table',
    **attrs,
):
    'Basecoat Table.'
    classes = ' '.join(filter(None, ('table', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def TableContainer(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Basecoat TableContainer.'
    classes = ' '.join(filter(None, ('table-container', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Tabs(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    "Root tabs container. It becomes horizontal or vertical based on the child tablist's aria-orientation ."
    classes = ' '.join(filter(None, ('tabs', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Textarea(
    *children,
    cls: str = "",
    tag: str = 'textarea',
    **attrs,
):
    'Basecoat Textarea.'
    classes = ' '.join(filter(None, ('textarea', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Toast(
    *children,
    category: Literal['error', 'loading'] | None = None,
    toast_swipe: Literal['x'] | None = None,
    cls: str = "",
    tag: str = 'li',
    **attrs,
):
    'Basecoat Toast.'
    if category is not None:
        attrs['data-category'] = _option('category', category, ('error', 'loading'))
    if toast_swipe is not None:
        attrs['data-toast-swipe'] = _option('toast_swipe', toast_swipe, ('x',))
    classes = ' '.join(filter(None, ('toast', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def ToastContent(
    *children,
    cls: str = "",
    tag: str = 'div',
    **attrs,
):
    'Basecoat ToastContent.'
    attrs.setdefault('role', 'status')
    classes = ' '.join(filter(None, ('toast-content', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def Trace(
    *children,
    cls: str = "",
    tag: str = 'ol',
    **attrs,
):
    'Basecoat Trace.'
    attrs.setdefault('role', 'list')
    classes = ' '.join(filter(None, ('trace', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)


def TraceLine(
    *children,
    cls: str = "",
    tag: str = 'summary',
    **attrs,
):
    'Basecoat TraceLine.'
    classes = ' '.join(filter(None, ('trace-line', cls)))
    return ft_html(tag, *children, cls=classes, **attrs)
