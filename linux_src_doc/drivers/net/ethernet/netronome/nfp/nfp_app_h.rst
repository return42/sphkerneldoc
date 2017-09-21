.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_app.h

.. _`nfp_app_type`:

struct nfp_app_type
===================

.. c:type:: struct nfp_app_type

    application definition

.. _`nfp_app_type.definition`:

Definition
----------

.. code-block:: c

    struct nfp_app_type {
        enum nfp_app_id id;
        const char *name;
        bool ctrl_has_meta;
        int (*init)(struct nfp_app *app);
        void (*clean)(struct nfp_app *app);
        const char *(*extra_cap)(struct nfp_app *app, struct nfp_net *nn);
        int (*vnic_alloc)(struct nfp_app *app, struct nfp_net *nn, unsigned int id);
        void (*vnic_free)(struct nfp_app *app, struct nfp_net *nn);
        int (*vnic_init)(struct nfp_app *app, struct nfp_net *nn);
        void (*vnic_clean)(struct nfp_app *app, struct nfp_net *nn);
        int (*repr_open)(struct nfp_app *app, struct nfp_repr *repr);
        int (*repr_stop)(struct nfp_app *app, struct nfp_repr *repr);
        int (*start)(struct nfp_app *app);
        void (*stop)(struct nfp_app *app);
        void (*ctrl_msg_rx)(struct nfp_app *app, struct sk_buff *skb);
        int (*setup_tc)(struct nfp_app *app, struct net_device *netdev, enum tc_setup_type type, void *type_data);
        bool (*tc_busy)(struct nfp_app *app, struct nfp_net *nn);
        int (*xdp_offload)(struct nfp_app *app, struct nfp_net *nn, struct bpf_prog *prog);
        int (*sriov_enable)(struct nfp_app *app, int num_vfs);
        void (*sriov_disable)(struct nfp_app *app);
        enum devlink_eswitch_mode (*eswitch_mode_get)(struct nfp_app *app);
        struct net_device *(*repr_get)(struct nfp_app *app, u32 id);
    }

.. _`nfp_app_type.members`:

Members
-------

id
    application ID

name
    application name

ctrl_has_meta
    control messages have prepend of type:5/port:CTRL

init
    perform basic app checks and init

clean
    clean app state

extra_cap
    extra capabilities string

vnic_alloc
    allocate vNICs (assign port types, etc.)

vnic_free
    free up app's vNIC state

vnic_init
    vNIC netdev was registered

vnic_clean
    vNIC netdev about to be unregistered

repr_open
    representor netdev open callback

repr_stop
    representor netdev stop callback

start
    start application logic

stop
    stop application logic

ctrl_msg_rx
    control message handler

setup_tc
    setup TC ndo

tc_busy
    TC HW offload busy (rules loaded)

xdp_offload
    offload an XDP program

sriov_enable
    app-specific sriov initialisation

sriov_disable
    app-specific sriov clean-up

eswitch_mode_get
    get SR-IOV eswitch mode

repr_get
    get representor netdev

.. _`nfp_app_type.description`:

Description
-----------

Callbacks

.. _`nfp_app`:

struct nfp_app
==============

.. c:type:: struct nfp_app

    NFP application container

.. _`nfp_app.definition`:

Definition
----------

.. code-block:: c

    struct nfp_app {
        struct pci_dev *pdev;
        struct nfp_pf *pf;
        struct nfp_cpp *cpp;
        struct nfp_net *ctrl;
        struct nfp_reprs __rcu  *reprs;
        const struct nfp_app_type *type;
        void *priv;
    }

.. _`nfp_app.members`:

Members
-------

pdev
    backpointer to PCI device

pf
    backpointer to NFP PF structure

cpp
    pointer to the CPP handle

ctrl
    pointer to ctrl vNIC struct

reprs
    array of pointers to representors

type
    pointer to const application ops and info

priv
    app-specific priv data

.. This file was automatic generated / don't edit.

