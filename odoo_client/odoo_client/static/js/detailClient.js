$(document).ready(function () {
    $("#cc").inputmask({
        mask: "99A9999999-99/99",
        // placeholder: "##A#######-##/##",
        clearMaskOnLostFocus: true
    })

    $('#est_particulier').change(
        function () {
            if ($(this).is(':checked')) {
                $('#basic_info').after(`
                <div id="is_professional_non_commercial" style="display: flex; justify-content: space-around; margin-bottom: 5%">
                <div id="titles" style="display: flex; justify-content: space-around; flex-direction: column">
                  <h6></h6>
                  <h6 id="label_ID">N° Identité</h6>
                </div>
                <div id="titles_info" style="display: flex; justify-content: space-around; flex-direction: column">
                <div><label for="professional_non_commercial" style="margin-right:1%">Est professional non commercial ?</label
                ><input type="checkbox" id="professional_non_commercial" name="professional_non_commercial" /></div>
                <input
                id="input_ID"
                type="text"
                class="form-control"
                required
              />
                </div>
              </div>
                `)
                $('#professional_non_commercial').change(
                    function () {
                        if ($(this).is(':checked')) {
                            $('#label_ID').attr("hidden", true);
                            $('#input_ID').attr("hidden", true);
                            $('#label_ID').after(`
                            <h6 id="ID_pro_title">N° ID professionel</h6>
                            <h6 id="ID_date_title">Date de délivrance</h6>
                            <h6 id="ID_authority_title">Autotrité délivrante</h6>
                            `)
                            $('#input_ID').after(`
                            <input
                                id="ID_pro"
                                type="text"
                                class="form-control"
                                required
                            />
                            <input
                                id="ID_date"
                                type="date"
                                class="form-control"
                                required
                            />
                            <input
                                id="ID_authority"
                                type="text"
                                class="form-control"
                                required
                            />
                                            `)

                        } else {
                            $('#label_ID').removeAttr('hidden');
                            $('#input_ID').removeAttr('hidden');
                            $('#ID_pro_title').attr("hidden", true);
                            $('#ID_date_title').attr("hidden", true);
                            $('#ID_authority_title').attr("hidden", true);
                            $('#ID_pro').attr("hidden", true);
                            $('#ID_date').attr("hidden", true);
                            $('#ID_authority').attr("hidden", true);
                        }
                    });
            } else {
                $('#is_professional_non_commercial').remove()
            }
        });

    $('#professional_non_commercial').change(
        function () {
            if ($(this).is(':checked')) {
                $('#label_ID').attr("hidden", true);
                $('#input_ID').attr("hidden", true);
            } else {
                $('#label_ID').removeAttr('hidden');
                $('#input_ID').removeAttr('hidden');
            }
        });


})