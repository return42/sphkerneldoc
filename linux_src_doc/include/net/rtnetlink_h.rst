.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/net/rtnetlink.h

.. _`rtnl_link_ops`:

struct rtnl_link_ops
====================

.. c:type:: struct rtnl_link_ops

    rtnetlink link operations

.. _`rtnl_link_ops.definition`:

Definition
----------

.. code-block:: c

    struct rtnl_link_ops {
        struct list_head list;
        const char *kind;
        size_t priv_size;
        void (*setup)(struct net_device *dev);
        int maxtype;
        const struct nla_policy *policy;
        int (*validate)(struct nlattr *tb[],struct nlattr *data[]);
        int (*newlink)(struct net *src_net,struct net_device *dev,struct nlattr *tb[],struct nlattr *data[]);
        int (*changelink)(struct net_device *dev,struct nlattr *tb[],struct nlattr *data[]);
        void (*dellink)(struct net_device *dev,struct list_head *head);
        size_t (*get_size)(const struct net_device *dev);
        int (*fill_info)(struct sk_buff *skb,const struct net_device *dev);
        size_t (*get_xstats_size)(const struct net_device *dev);
        int (*fill_xstats)(struct sk_buff *skb,const struct net_device *dev);
        unsigned int (*get_num_tx_queues)(void);
        unsigned int (*get_num_rx_queues)(void);
        int slave_maxtype;
        const struct nla_policy *slave_policy;
        int (*slave_validate)(struct nlattr *tb[],struct nlattr *data[]);
        int (*slave_changelink)(struct net_device *dev,struct net_device *slave_dev,struct nlattr *tb[],struct nlattr *data[]);
        size_t (*get_slave_size)(const struct net_device *dev,const struct net_device *slave_dev);
        int (*fill_slave_info)(struct sk_buff *skb,const struct net_device *dev,const struct net_device *slave_dev);
        struct net *(*get_link_net)(const struct net_device *dev);
        size_t (*get_linkxstats_size)(const struct net_device *dev,int attr);
        int (*fill_linkxstats)(struct sk_buff *skb,const struct net_device *dev,int *prividx, int attr);
    }

.. _`rtnl_link_ops.members`:

Members
-------

list
    Used internally

kind
    Identifier

priv_size
    sizeof net_device private space

setup
    net_device setup function

maxtype
    Highest device specific netlink attribute number

policy
    Netlink policy for device specific attribute validation

validate
    Optional validation function for netlink/changelink parameters

newlink
    Function for configuring and registering a new device

changelink
    Function for changing parameters of an existing device

dellink
    Function to remove a device

get_size
    Function to calculate required room for dumping device
    specific netlink attributes

fill_info
    Function to dump device specific netlink attributes

get_xstats_size
    Function to calculate required room for dumping device
    specific statistics

fill_xstats
    Function to dump device specific statistics

get_num_tx_queues
    Function to determine number of transmit queues
    to create when creating a new device.

get_num_rx_queues
    Function to determine number of receive queues
    to create when creating a new device.

slave_maxtype
    *undescribed*

slave_policy
    *undescribed*

slave_validate
    *undescribed*

slave_changelink
    *undescribed*

get_slave_size
    *undescribed*

fill_slave_info
    *undescribed*

get_link_net
    Function to get the i/o netns of the device

get_linkxstats_size
    Function to calculate the required room for
    dumping device-specific extended link stats

fill_linkxstats
    Function to dump device-specific extended link stats

.. _`rtnl_af_ops`:

struct rtnl_af_ops
==================

.. c:type:: struct rtnl_af_ops

    rtnetlink address family operations

.. _`rtnl_af_ops.definition`:

Definition
----------

.. code-block:: c

    struct rtnl_af_ops {
        struct list_head list;
        int family;
        int (*fill_link_af)(struct sk_buff *skb,const struct net_device *dev,u32 ext_filter_mask);
        size_t (*get_link_af_size)(const struct net_device *dev,u32 ext_filter_mask);
        int (*validate_link_af)(const struct net_device *dev,const struct nlattr *attr);
        int (*set_link_af)(struct net_device *dev,const struct nlattr *attr);
    }

.. _`rtnl_af_ops.members`:

Members
-------

list
    Used internally

family
    Address family

fill_link_af
    Function to fill IFLA_AF_SPEC with address family
    specific netlink attributes.

get_link_af_size
    Function to calculate size of address family specific
    netlink attributes.

validate_link_af
    Validate a IFLA_AF_SPEC attribute, must check attr
    for invalid configuration settings.

set_link_af
    Function to parse a IFLA_AF_SPEC attribute and modify
    net_device accordingly.

.. This file was automatic generated / don't edit.

