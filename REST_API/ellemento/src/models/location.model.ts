import {Entity, model, property, hasMany} from '@loopback/repository';
import {LocationStageAssignment} from './location-stage-assignment.model';
import {TrayMovement} from './tray-movement.model';
import {Tray} from './tray.model';
import {LightHistory} from './light-history.model';
import {VentilationHistory} from './ventilation-history.model';
import {WaterHistory} from './water-history.model';

@model({settings: {strict: false}})
export class Location extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  location_id?: number;

  @property({
    type: 'number',
    required: true,
  })
  bay_id: number;

  @property({
    type: 'number',
    required: true,
  })
  container_id: number;

  @property({
    type: 'number',
    required: true,
  })
  shelf_id: number;

  @property({
    type: 'number',
    required: true,
  })
  slot_num: number;

  @property({
    type: 'string',
  })
  comment?: string;

  @hasMany(() => LocationStageAssignment)
  locationStageAssignments: LocationStageAssignment[];

  @hasMany(() => TrayMovement)
  trayMovements: TrayMovement[];

  @hasMany(() => Tray)
  trays: Tray[];

  @hasMany(() => LightHistory)
  lightHistories: LightHistory[];

  @hasMany(() => VentilationHistory)
  ventilationHistories: VentilationHistory[];

  @hasMany(() => WaterHistory)
  waterHistories: WaterHistory[];

  @property({
    type: 'number',
  })
  shelfId?: number;
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<Location>) {
    super(data);
  }
}

export interface LocationRelations {
  // describe navigational properties here
}

export type LocationWithRelations = Location & LocationRelations;
