function D(m, n) {
    result = 0;
    for (let i = 0; i < m; i++) {
        result += Math.floor(1 + Math.random() * n)
    }
    return result;
}

function random_generate() {
    var strength = 5 * D(3, 6);
    var consitution = 5 * D(3, 6);
    var dexterity = 5 * D(3, 6);
    var appearance = 5 * D(3, 6);
    var power = 5 * D(3, 6);
    var size = 5 * (D(2, 6) + 6);
    var intelligence = 5 * (D(2, 6) + 6);
    var education = 5 * (D(2, 6) + 6);
    var luck = 5 * D(3, 6);

    document.getElementById("id_strength").value = strength;
    document.getElementById("id_constitution").value = consitution;
    document.getElementById("id_dexterity").value = dexterity;
    document.getElementById("id_appearance").value = appearance;
    document.getElementById("id_power").value = power;
    document.getElementById("id_size").value = size;
    document.getElementById("id_intelligence").value = intelligence;
    document.getElementById("id_education").value = education;
    document.getElementById("id_luck").value = luck;
    document.getElementById("id_total").value = strength + consitution + dexterity + appearance
                                                + power + size + intelligence + education + luck;

    document.getElementById("id_dodge").value = Math.floor(dexterity / 2);
    document.getElementById("id_language").value = education;

    document.getElementById("id_max_hp").value = Math.floor((size + consitution) / 10);
    document.getElementById("id_curr_hp").value = Math.floor((size + consitution) / 10);
    document.getElementById("id_max_mp").value = Math.floor(power / 5);
    document.getElementById("id_curr_mp").value = Math.floor(power / 5);
    document.getElementById("id_max_sanity").value = power;
    document.getElementById("id_curr_sanity").value = power;
}

function calculate_avaliable_skill_points() {
    // calculate used skill points
    var initial_skill_points = 432
                                + Math.floor(parseInt(document.getElementById("id_dexterity").value) / 2)
                                + parseInt(document.getElementById("id_education").value);
    var used_skill_points = 0
    var skills = document.getElementsByClassName("skill");
    for (let i = 0; i < skills.length; i++) {
        used_skill_points += parseInt(skills[i].value);
    }
    used_skill_points -= initial_skill_points

    // calculate available skill points
    var total_available_skill_points = parseInt(document.getElementById("id_total_skill_points").value);
    var current_available_skill_points = total_available_skill_points - used_skill_points;
    document.getElementById("id_available_skill_points").value = current_available_skill_points;
}