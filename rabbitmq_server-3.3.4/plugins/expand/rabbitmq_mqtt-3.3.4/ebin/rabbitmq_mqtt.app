{application,rabbitmq_mqtt,
    [{description,"RabbitMQ MQTT Adapter"},
     {vsn,"3.3.4"},
     {modules,
         [rabbit_mqtt,rabbit_mqtt_collector,rabbit_mqtt_connection_sup,
          rabbit_mqtt_frame,rabbit_mqtt_processor,rabbit_mqtt_reader,
          rabbit_mqtt_sup,rabbit_mqtt_util]},
     {registered,[]},
     {mod,{rabbit_mqtt,[]}},
     {env,
         [{default_user,<<"guest">>},
          {default_pass,<<"guest">>},
          {allow_anonymous,true},
          {vhost,<<"/">>},
          {exchange,<<"amq.topic">>},
          {subscription_ttl,1800000},
          {prefetch,10},
          {ssl_listeners,[]},
          {tcp_listeners,[1883]},
          {tcp_listen_options,
              [binary,
               {packet,raw},
               {reuseaddr,true},
               {backlog,128},
               {nodelay,true}]}]},
     {applications,[kernel,stdlib,rabbit,amqp_client]}]}.