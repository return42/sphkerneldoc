.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/console.h

.. _`consw`:

struct consw
============

.. c:type:: struct consw

    callbacks for consoles

.. _`consw.definition`:

Definition
----------

.. code-block:: c

    struct consw {
        struct module *owner;
        const char *(*con_startup)(void);
        void (*con_init)(struct vc_data *vc, int init);
        void (*con_deinit)(struct vc_data *vc);
        void (*con_clear)(struct vc_data *vc, int sy, int sx, int height, int width);
        void (*con_putc)(struct vc_data *vc, int c, int ypos, int xpos);
        void (*con_putcs)(struct vc_data *vc, const unsigned short *s, int count, int ypos, int xpos);
        void (*con_cursor)(struct vc_data *vc, int mode);
        bool (*con_scroll)(struct vc_data *vc, unsigned int top,unsigned int bottom, enum con_scroll dir, unsigned int lines);
        int (*con_switch)(struct vc_data *vc);
        int (*con_blank)(struct vc_data *vc, int blank, int mode_switch);
        int (*con_font_set)(struct vc_data *vc, struct console_font *font, unsigned int flags);
        int (*con_font_get)(struct vc_data *vc, struct console_font *font);
        int (*con_font_default)(struct vc_data *vc, struct console_font *font, char *name);
        int (*con_font_copy)(struct vc_data *vc, int con);
        int (*con_resize)(struct vc_data *vc, unsigned int width, unsigned int height, unsigned int user);
        void (*con_set_palette)(struct vc_data *vc, const unsigned char *table);
        void (*con_scrolldelta)(struct vc_data *vc, int lines);
        int (*con_set_origin)(struct vc_data *vc);
        void (*con_save_screen)(struct vc_data *vc);
        u8 (*con_build_attr)(struct vc_data *vc, u8 color, u8 intensity, u8 blink, u8 underline, u8 reverse, u8 italic);
        void (*con_invert_region)(struct vc_data *vc, u16 *p, int count);
        u16 *(*con_screen_pos)(struct vc_data *vc, int offset);
        unsigned long (*con_getxy)(struct vc_data *vc, unsigned long position, int *px, int *py);
        void (*con_flush_scrollback)(struct vc_data *vc);
        int (*con_debug_enter)(struct vc_data *vc);
        int (*con_debug_leave)(struct vc_data *vc);
    }

.. _`consw.members`:

Members
-------

owner
    *undescribed*

con_startup
    *undescribed*

con_init
    *undescribed*

con_deinit
    *undescribed*

con_clear
    *undescribed*

con_putc
    *undescribed*

con_putcs
    *undescribed*

con_cursor
    *undescribed*

con_scroll
    move lines from \ ``top``\  to \ ``bottom``\  in direction \ ``dir``\  by \ ``lines``\ .
    Return true if no generic handling should be done.
    Invoked by csi_M and printing to the console.

con_switch
    *undescribed*

con_blank
    *undescribed*

con_font_set
    *undescribed*

con_font_get
    *undescribed*

con_font_default
    *undescribed*

con_font_copy
    *undescribed*

con_resize
    *undescribed*

con_set_palette
    sets the palette of the console to \ ``table``\  (optional)

con_scrolldelta
    the contents of the console should be scrolled by \ ``lines``\ .
    Invoked by user. (optional)

con_set_origin
    *undescribed*

con_save_screen
    *undescribed*

con_build_attr
    *undescribed*

con_invert_region
    *undescribed*

con_screen_pos
    *undescribed*

con_getxy
    *undescribed*

con_flush_scrollback
    *undescribed*

con_debug_enter
    *undescribed*

con_debug_leave
    *undescribed*

.. This file was automatic generated / don't edit.

