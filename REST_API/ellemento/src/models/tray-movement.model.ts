import {Entity, model, property} from '@loopback/repository';

@model({settings: {strict: false}})
export class TrayMovement extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  tray_movement_id?: number;

  @property({
    type: 'number',
    required: true,
  })
  tray_id: number;

  @property({
    type: 'number',
    required: true,
  })
  state_id: number;

  @property({
    type: 'number',
    required: true,
  })
  source_location_id: number;

  @property({
    type: 'number',
    required: true,
  })
  destination_location_id: number;

  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<TrayMovement>) {
    super(data);
  }
}

export interface TrayMovementRelations {
  // describe navigational properties here
}

export type TrayMovementWithRelations = TrayMovement & TrayMovementRelations;
