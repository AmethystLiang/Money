{application,rabbitmq_management_agent,
             [{description,"RabbitMQ Management Agent"},
              {vsn,"3.3.4"},
              {modules,[rabbit_mgmt_agent_app,rabbit_mgmt_agent_sup,
                        rabbit_mgmt_db_handler,rabbit_mgmt_external_stats]},
              {registered,[]},
              {mod,{rabbit_mgmt_agent_app,[]}},
              {env,[{force_fine_statistics,true}]},
              {applications,[kernel,stdlib,rabbit]}]}.
