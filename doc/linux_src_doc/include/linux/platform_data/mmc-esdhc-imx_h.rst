.. -*- coding: utf-8; mode: rst -*-

===============
mmc-esdhc-imx.h
===============


.. _`esdhc_platform_data`:

struct esdhc_platform_data
==========================

.. c:type:: esdhc_platform_data

    platform data for esdhc on i.MX


.. _`esdhc_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct esdhc_platform_data {
    unsigned int wp_gpio;
    unsigned int cd_gpio;
    enum wp_types wp_type;
    enum cd_types cd_type;
    bool support_vsel;
  };


.. _`esdhc_platform_data.members`:

Members
-------

:``wp_gpio``:
    gpio for write_protect

:``cd_gpio``:
    gpio for card_detect interrupt

:``wp_type``:
    type of write_protect method (see wp_types enum above)

:``cd_type``:
    type of card_detect method (see cd_types enum above)

:``support_vsel``:
    indicate it supports 1.8v switching




.. _`esdhc_platform_data.description`:

Description
-----------


ESDHC_WP(CD)_CONTROLLER type is not available on i.MX25/35.

