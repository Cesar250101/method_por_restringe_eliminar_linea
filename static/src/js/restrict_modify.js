odoo.define('method_por_restringe_eliminar_linea.restrict_modify', function(require){
    'use strict';

    var screens = require('point_of_sale.screens');
    var rpc = require('web.rpc')

    screens.NumpadWidget.include({

        renderElement: function(){
            this._super();
            var $self = this;
            rpc.query({
             model: 'pos.order',
             method: 'get_user_group',
             args :[self.posmodel.user.id],
             }).then(function(data){
                if(!data){
                   $self.$('.numpad-backspace').hide();
                }
            });
        }

    });


});