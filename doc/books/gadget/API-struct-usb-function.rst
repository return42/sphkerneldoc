
.. _API-struct-usb-function:

===================
struct usb_function
===================

*man struct usb_function(9)*

*4.6.0-rc1*

describes one function of a configuration


Synopsis
========

.. code-block:: c

    struct usb_function {
      const char * name;
      struct usb_gadget_strings ** strings;
      struct usb_descriptor_header ** fs_descriptors;
      struct usb_descriptor_header ** hs_descriptors;
      struct usb_descriptor_header ** ss_descriptors;
      struct usb_descriptor_header ** ssp_descriptors;
      struct usb_configuration * config;
      struct usb_os_desc_table * os_desc_table;
      unsigned os_desc_n;
      int (* bind) (struct usb_configuration *,struct usb_function *);
      void (* unbind) (struct usb_configuration *,struct usb_function *);
      void (* free_func) (struct usb_function *f);
      struct module * mod;
      int (* set_alt) (struct usb_function *,unsigned interface, unsigned alt);
      int (* get_alt) (struct usb_function *,unsigned interface);
      void (* disable) (struct usb_function *);
      int (* setup) (struct usb_function *,const struct usb_ctrlrequest *);
      bool (* req_match) (struct usb_function *,const struct usb_ctrlrequest *);
      void (* suspend) (struct usb_function *);
      void (* resume) (struct usb_function *);
      int (* get_status) (struct usb_function *);
      int (* func_suspend) (struct usb_function *,u8 suspend_opt);
    };


Members
=======

name
    For diagnostics, identifies the function.

strings
    tables of strings, keyed by identifiers assigned during ``bind`` and by language IDs provided in control requests

fs_descriptors
    Table of full (or low) speed descriptors, using interface and string identifiers assigned during ``bind``\ (). If this pointer is null, the function will not be available at
    full speed (or at low speed).

hs_descriptors
    Table of high speed descriptors, using interface and string identifiers assigned during ``bind``\ (). If this pointer is null, the function will not be available at high speed.

ss_descriptors
    Table of super speed descriptors, using interface and string identifiers assigned during ``bind``\ (). If this pointer is null after initiation, the function will not be
    available at super speed.

ssp_descriptors
    Table of super speed plus descriptors, using interface and string identifiers assigned during ``bind``\ (). If this pointer is null after initiation, the function will not be
    available at super speed plus.

config
    assigned when ``usb_add_function``\ () is called; this is the configuration with which this function is associated.

os_desc_table
    Table of (interface id, os descriptors) pairs. The function can expose more than one interface. If an interface is a member of an IAD, only the first interface of IAD has its
    entry in the table.

os_desc_n
    Number of entries in os_desc_table

bind
    Before the gadget can register, all of its functions ``bind`` to the available resources including string and interface identifiers used in interface or class descriptors;
    endpoints; I/O buffers; and so on.

unbind
    Reverses ``bind``; called as a side effect of unregistering the driver which added this function.

free_func
    free the struct usb_function.

mod
    (internal) points to the module that created this structure.

set_alt
    (REQUIRED) Reconfigures altsettings; function drivers may initialize usb_ep.driver data at this time (when it is used). Note that setting an interface to its current
    altsetting resets interface state, and that all interfaces have a disabled state.

get_alt
    Returns the active altsetting. If this is not provided, then only altsetting zero is supported.

disable
    (REQUIRED) Indicates the function should be disabled. Reasons include host resetting or reconfiguring the gadget, and disconnection.

setup
    Used for interface-specific control requests.

req_match
    Tests if a given class request can be handled by this function.

suspend
    Notifies functions when the host stops sending USB traffic.

resume
    Notifies functions when the host restarts USB traffic.

get_status
    Returns function status as a reply to ``GetStatus`` request when the recipient is Interface.

func_suspend
    callback to be called when SetFeature(FUNCTION_SUSPEND) is reseived


Description
===========

A single USB function uses one or more interfaces, and should in most cases support operation at both full and high speeds. Each function is associated by ``usb_add_function``\ ()
with a one configuration; that function causes ``bind``\ () to be called so resources can be allocated as part of setting up a gadget driver. Those resources include endpoints,
which should be allocated using ``usb_ep_autoconfig``\ ().

To support dual speed operation, a function driver provides descriptors for both high and full speed operation. Except in rare cases that don't involve bulk endpoints, each speed
needs different endpoint descriptors.

Function drivers choose their own strategies for managing instance data. The simplest strategy just declares it "static', which means the function can only be activated once. If
the function needs to be exposed in more than one configuration at a given speed, it needs to support multiple usb_function structures (one for each configuration).

A more complex strategy might encapsulate a ``usb_function`` structure inside a driver-specific instance structure to allows multiple activations. An example of multiple
activations might be a CDC ACM function that supports two or more distinct instances within the same configuration, providing several independent logical data links to a USB host.
