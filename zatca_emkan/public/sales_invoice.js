frappe.ui.form.on('Sales Invoice', {
    refresh: async function (frm) {
        // Only proceed if invoice is submitted
        if (frm.doc.docstatus !== 1) return;

        // Await the async calls properly
        const customerRes = await frappe.db.get_value("Customer", frm.doc.customer, "dont_send_to_zatca");
        const dontSend = customerRes.message?.dont_send_to_zatca;
        if (dontSend == 1) return;

        const siafRes = await frappe.db.get_value(
            'Sales Invoice Additional Fields',
            { sales_invoice: frm.doc.name },
            'name'
        );
        const siaf_name = siafRes.message?.name;
        if (!siaf_name) return;

        // Add button only if all checks pass
        let btn = frm.add_custom_button(__('Zatca PDF/XML'), async function () {
            await frappe.call({
                method: 'ksa_compliance.ksa_compliance.doctype.sales_invoice_additional_fields.sales_invoice_additional_fields.check_pdf_a3b_support',
                args: { id: siaf_name }
            });

            let fields = [
                {
                    label: 'Print Format',
                    fieldname: 'print_format',
                    fieldtype: 'Link',
                    options: 'Print Format',
                    reqd: 1,
                },
                {
                    label: 'Language',
                    fieldname: 'lang',
                    fieldtype: 'Link',
                    options: 'Language',
                    default: 'en',
                    reqd: 1,
                }
            ];

            frappe.prompt(fields, values => {
                window.location.assign(
                    "/api/method/ksa_compliance.ksa_compliance.doctype.sales_invoice_additional_fields.sales_invoice_additional_fields.download_zatca_pdf" +
                    "?id=" + siaf_name +
                    "&print_format=" + values.print_format +
                    "&lang=" + values.lang
                );
            });
        });

        $(btn).removeClass('btn-default').addClass('btn-success');
    }
});