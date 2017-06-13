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
        void (*con_init)(struct vc_data *, int);
        void (*con_deinit)(struct vc_data *);
        void (*con_clear)(struct vc_data *, int, int, int, int);
        void (*con_putc)(struct vc_data *, int, int, int);
        void (*con_putcs)(struct vc_data *, const unsigned short *, int, int, int);
        void (*con_cursor)(struct vc_data *, int);
        bool (*con_scroll)(struct vc_data *, unsigned int top,unsigned int bottom, enum con_scroll dir, unsigned int lines);
        int (*con_switch)(struct vc_data *);
        int (*con_blank)(struct vc_data *, int, int);
        int (*con_font_set)(struct vc_data *, struct console_font *, unsigned);
        int (*con_font_get)(struct vc_data *, struct console_font *);
        int (*con_font_default)(struct vc_data *, struct console_font *, char *);
        int (*con_font_copy)(struct vc_data *, int);
        int (*con_resize)(struct vc_data *, unsigned int, unsigned int, unsigned int);
        void (*con_set_palette)(struct vc_data *, const unsigned char *table);
        void (*con_scrolldelta)(struct vc_data *, int lines);
        int (*con_set_origin)(struct vc_data *);
        void (*con_save_screen)(struct vc_data *);
        u8 (*con_build_attr)(struct vc_data *, u8, u8, u8, u8, u8, u8);
        void (*con_invert_region)(struct vc_data *, u16 *, int);
        u16 *(*con_screen_pos)(struct vc_data *, int);
        unsigned long (*con_getxy)(struct vc_data *, unsigned long, int *, int *);
        void (*con_flush_scrollback)(struct vc_data *);
        int (*con_debug_enter)(struct vc_data *);
        int (*con_debug_leave)(struct vc_data *);
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

